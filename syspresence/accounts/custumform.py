from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    ROLE_CHOICES = [
        ('enseignant', 'Enseignant'),
        ('educateur', 'Educateur'),
        ('parent','Parent')
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'placeholder': 'Sélectionnez votre rôle',
            'class': 'input',  # Optionnel : pour ajouter des styles CSS
        })
    )

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        # Supprime les labels et ajoute des placeholders pour chaque champ
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nom et prénom',
            'class': 'input',  # Optionnel : ajouter une classe CSS
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Mot de passe',
            'class': 'input',
        })
        self.fields['role'].widget.attrs.update({
            'class': 'input select',  # Exemple pour un menu déroulant
        })

        # Optionnel : Supprimer les labels
        for field in self.fields.values():
            field.label = ""
