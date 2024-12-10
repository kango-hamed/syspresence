from django.contrib import admin
from .models import Notification, Etudiant, Presences, Rapport


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'write_by','send_to', 'created_at', 'is_read','is_archived')  # Colonnes à afficher
    list_filter = ('is_read', 'created_at','is_archived')  # Filtres disponibles
    search_fields = ('title', 'message', 'write_by__username','send_to__username')  # Champs de recherche

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    # Affiche automatiquement tous les champs du modèle Etudiant
    fields = [field.name for field in Etudiant._meta.get_fields()]


@admin.register(Presences)
class PresencesAdmin(admin.ModelAdmin):
    # Affiche automatiquement tous les champs du modèle Presences
    fields = [field.name for field in Presences._meta.get_fields()]


@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    fields = [field.name for field in Rapport._meta.get_fields()]