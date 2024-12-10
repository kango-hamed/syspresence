from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Ajout du champ "role" au formulaire d'administration
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']

