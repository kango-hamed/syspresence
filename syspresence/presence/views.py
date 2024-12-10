from django.shortcuts import render
from .models import Notification
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings

def ajouter_notification(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")
        write_by_id = request.POST.get("write_by")  # ID de l'expéditeur
        send_to_id = request.POST.get("send_to")  # ID du destinataire

        # Récupérer les utilisateurs
        write_by = get_object_or_404(request.user.username, id=write_by_id)
        send_to = get_object_or_404(request.user.username, id=send_to_id)

        try:
            # Appeler la méthode envoyer
            notification = Notification.envoyer(
                title=title,
                message=message,
                write_by=write_by,
                send_to=send_to
            )
            return JsonResponse({"success": True, "message": "Notification ajoutée avec succès."})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Requête invalide"})

def get_new_template(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'educateur/messagesForm.html')
    return JsonResponse({'error': 'Requête invalide'}, status=400)

def notification_partial(request, notification_id):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        notification = get_object_or_404(Notification, id = notification_id)
        return render(request, 'educateur/messagesDisplay.html', {'notification': notification})
    return JsonResponse({'error': 'Requête invalide'}, status=400)

def get_notification_details(request, notification_id):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Vérifie que c'est une requête AJAX
        try:
            notification = get_object_or_404(Notification, id = notification_id)
            data = {
                'user': request.user.username,  # Assurez-vous que ceci est correct
                'title': notification.title,
                'message': notification.message,
                'write_by': notification.write_by.username,
                'send_to': notification.send_to.username,
                'created_at': notification.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'is_archived': notification.is_archived,
                'is_read': notification.is_read
            }
            return JsonResponse(data)
        except Notification.DoesNotExist:
            return JsonResponse({'error': 'Notification not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def render_by_role(request, templates, context = None):
    user = request.user
    if user.is_authenticated:
        return render(request, templates.get(user.role, 'default_template.html'),context)
    return render(request, 'accounts/login.html')

def dashboard(request):
    templates = {
        'enseignant': 'enseignant/dashboard.html',
        'educateur': 'educateur/dashboard.html',
        'parent': 'parent/dashboard.html',
    }
    return render_by_role(request, templates)


def etudiants(request):
    templates = {
        'enseignant': 'enseignant/etudiants.html',
        'educateur': 'educateur/etudiants.html',
        'parent': 'parent/etudiants.html',
    }
    return render_by_role(request, templates)

def notifications(request):
    notifications = Notification.objects.all()
    templates = {
        'educateur': 'educateur/notifications.html',
    }
    return render_by_role(request, templates, {'notifications':notifications})

def presences(request):

    templates = {
        'enseignant': 'enseignant/presences.html',
        'educateur': 'educateur/presences.html',
        'parent': 'parent/presences.html',
    }
    return render_by_role(request, templates)

def rapports(request):
    templates = {
        'enseignant': 'enseignant/rapports.html',
        'educateur': 'educateur/rapports.html',
        'parent': 'parent/rapports.html',
    }
    return render_by_role(request, templates)

def settings(request):
    templates = {
        'enseignant': 'enseignant/settings.html',
        'educateur': 'educateur/settings.html',
        'parent': 'parent/settings.html',
    }
    return render_by_role(request, templates)