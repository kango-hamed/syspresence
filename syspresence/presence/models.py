from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Etudiant(models.Model):
    class Filiere(models.TextChoices):
        SRIT = 'SRIT'
        TWIN = 'TWIN'
        RTEL = 'RTEL'
        SIGL = 'SIGL'
        SITW = 'SITW'

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    filiere = models.CharField(choices=Filiere.choices, max_length=10)
    niveau = models.CharField(max_length=10)
    classe = models.CharField(max_length=10)
    regularite = models.CharField(max_length=10)

    def enregistrer_presence(self):
        pass

    def generer_rapport(self):
        pass

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.classe}"


class Presences(models.Model):
    class Etat(models.TextChoices):
        PRESENT = 'PRESENT'
        ABSENT = 'ABSENT'
        RETARD = 'RETARD'

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='presences')
    date = models.DateField()
    heure = models.TimeField()
    etat = models.CharField(choices=Etat.choices, max_length=10, default=Etat.PRESENT)

    def enregistrer(self):
        pass

    def modifier_etat(self, nouvel_etat):
        self.etat = nouvel_etat
        self.save()

    def __str__(self):
        return f"Présence de {self.etudiant} le {self.date} à {self.heure}"


class Rapport(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='rapports')
    periode = models.CharField(max_length=50)
    statistiques = models.TextField()

    def generer(self):
        pass

    def telecharger(self):
        pass

    def __str__(self):
        return f"Rapport pour {self.etudiant} - Période : {self.periode}"

class Notification(models.Model):
    title = models.CharField(max_length=255)  # Titre de la notification
    message = models.TextField()  # Message détaillé
    write_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications_sent'
    )  # Expéditeur
    send_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications_received'
    )  # Destinataire
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    is_read = models.BooleanField(default=False)  # État de lecture
    is_archived = models.BooleanField(default=False)
    def __str__(self):
        return f"Notification à {self.send_to.username}: {self.title}"

    @classmethod
    def envoyer(cls, title, message, write_by, send_to):
        # Vérifier que les utilisateurs expéditeur et destinataire sont différents
        if write_by == send_to:
            raise ValidationError("L'expéditeur et le destinataire ne peuvent pas être les mêmes.")

        # Créer et sauvegarder la notification
        notification = cls.objects.create(
            title=title,
            message=message,
            write_by=write_by,
            send_to=send_to
        )
        return notification
        

    def archiver(self):
        """Logique pour archiver la notification."""
        # Implémentez ici ce qu'il faut pour marquer ou déplacer une notification comme archivée.
        pass

