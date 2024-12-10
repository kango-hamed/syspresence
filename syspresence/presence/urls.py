from django.contrib import admin
from django.urls import path
from . import views
app_name = 'presence'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('gestion-des-etudiants/', views.etudiants, name = 'etudiants'),
    path('presences/', views.presences, name = 'presences'),
    path('notifications/', views.notifications, name = 'notifications'),
    path('rapports/', views.rapports, name = 'rapports'),
    path('configuration/', views.settings, name = 'settings'),
    path('notification/<int:notification_id>/', views.get_notification_details, name='get_notification_details'),
    path('notifications/<int:notification_id>/', views.notification_partial, name='notification_partial'),
    path('notifications/get-new-template/', views.get_new_template, name='get_new_template'),
    path('notifications/ajouter-notification/', views.ajouter_notification, name='ajouter_notification'),

]