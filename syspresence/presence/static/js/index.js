/* FONCTIONS DE MANIPULATION */
const fetchNotification = async (notificationId) => {
    try {
        const response = await fetch(`/presence/notification/${notificationId}/`, { 
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' } // Indique que c'est une requête AJAX
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des données');
        }
        
        const data = await response.json();
        return data; // Retourne les données après avoir été récupérées
    } catch (error) {
        console.error('Erreur:', error);
        throw error; // Lance l'erreur pour être capturée par la fonction appelante
    }
}

const fetchMessages = async (notificationId) => {
    try {
        const response = await fetch(`/presence/notifications/${notificationId}/`, { 
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' } // Indique que c'est une requête AJAX
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des données');
        }
        
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Erreur:', error);
        throw error; // Lance l'erreur pour être capturée par la fonction appelante
    }
}
const fetchNewTemplate = async () => {
    try {
        const response = await fetch(`/presence/notifications/get-new-template/`, { 
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' } // Indique que c'est une requête AJAX
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des données');
        }
        
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Erreur:', error);
        throw error; // Lance l'erreur pour être capturée par la fonction appelante
    }
}

// Fonction pour gérer l'affichage des notifications
const handleDisplayNotification = async (notifications, btn) => {
    const btnContent = btn.innerText; // Texte du bouton
    for (const notification of notifications) {
        const notificationId = notification.getAttribute('data-id');
        try {
            const data = await fetchNotification(notificationId); // Attendez que les données soient récupérées

            const writer = data.write_by;
            const user = data.user;
            const is_archived = data.is_archived;

            // Logique de filtrage
            switch (btnContent) {
                case 'Boîte de réception':
                    if (writer !== user) {
                        notification.style.display = 'table-row'; // Afficher la ligne
                    } else {
                        notification.style.display = 'none'; // Masquer la ligne
                    }
                    break;

                case 'Messages envoyés':
                    if (writer === user) {
                        notification.style.display = 'table-row';
                    } else {
                        notification.style.display = 'none';
                    }
                    break;

                case 'Messages archivés':
                    if (Boolean(is_archived)) {
                        notification.style.display = 'table-row';
                    } else {
                        notification.style.display = 'none';
                    }
                    break;

                default:
                    notification.style.display = 'table-row'; // Afficher toutes les lignes
                    break;
            }
        } catch (error) {
            // Gérez l'erreur ici si nécessaire
            console.error("Erreur lors de l'affichage des notifications", error);
        }
    }
};

//
const handleDisplayMessages = async (notification, notificationDisplay) => {
    const notificationId = notification.getAttribute('data-id');
    const messageContainer = document.getElementById('messages-display');
    
    if (!messageContainer) {
        console.error('Erreur : Élément message non trouvé.');
        return;
    }

    try {
        const data = await fetchMessages(notificationId);
        // Affiche le message récupéré
        messageContainer.innerHTML = data;

        // Basculer l'affichage
        notificationDisplay.style.display = 'none';
        messageContainer.classList.add('messages-display');
        messageContainer.style.display = 'block';

        // Ajout de l'écouteur pour le bouton retour
        const btnReturn = document.getElementById('btn-return');
        if (btnReturn) {
            btnReturn.addEventListener('click', () => {
                messageContainer.classList.remove('messages-display');
                messageContainer.style.display = 'none';
                notificationDisplay.style.display = 'block';
            }, { once: true }); // Éviter les doublons
        } else {
            console.error("Bouton de retour introuvable.");
        }
    } catch (error) {
        console.error("Erreur lors de l'affichage du message :", error);
    }
};

/*const handleMessageForm = (form)=>{
    form.addEventListener('submit',(event)=>{
        event.preventDefault();
        const formData = new FormData(form)
        try {
            const data = fetchFormData()
        } 
        catch (error) {
            console.error("Erreur lors de l'affichage du formulaire :", error);
        }
    })
}
*/

const handleMessageFormDisplay = async (notificationDisplay)=>{
    const messageContainer = document.getElementById('messages-display');
    
    if (!messageContainer) {
        console.error('Erreur : Élément message non trouvé.');
        return;
    }

    try {
        const data = await fetchNewTemplate();
        messageContainer.innerHTML = data;
        notificationDisplay.style.display = 'none';
        messageContainer.classList.add('messages-display');
        messageContainer.style.display = 'block';
        const btnReturn = document.getElementById('btn-return');
        if (btnReturn) {
            btnReturn.addEventListener('click', () => {
                messageContainer.classList.remove('messages-display');
                messageContainer.style.display = 'none';
                notificationDisplay.style.display = 'block';
            }, { once: true }); // Éviter les doublons
        } else {
            console.error("Bouton de retour introuvable.");
        }
    } catch (error) {
        console.error("Erreur lors de l'affichage du message :", error);
    }
}

/* MANIPULATION DES NOTIFICATIONS */
// Sélection des boutons et notifications
const btnsMessages = document.querySelectorAll('.btn-messages');
const notificationDisplay = document.querySelector('#notifications-display')// Utilisez une classe ici
const notifications = document.querySelectorAll('#notifications-display .notification');
// Ajout des écouteurs d'événements sur les boutons
btnsMessages.forEach(btn => {
    btn.addEventListener('click', () => handleDisplayNotification(notifications, btn));
});


/* MANIPULATION DE LA LECTURE DES MESSAGES */
notifications.forEach(
    notifcation =>{
        notifcation.addEventListener('click',(e)=>{
            handleDisplayMessages(notifcation,notificationDisplay);
        });
    }
);

const btnNew = document.getElementById('btn-new-message');
btnNew.addEventListener('click',(event)=>{
    handleMessageFormDisplay(notificationDisplay);
})

