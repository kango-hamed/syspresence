# Generated by Django 5.1.3 on 2024-12-08 23:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('filiere', models.CharField(choices=[('SRIT', 'Srit'), ('TWIN', 'Twin'), ('RTEL', 'Rtel'), ('SIGL', 'Sigl'), ('SITW', 'Sitw')], max_length=10)),
                ('niveau', models.CharField(max_length=10)),
                ('classe', models.CharField(max_length=10)),
                ('regularite', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('etat', models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('RETARD', 'Retard')], default='PRESENT', max_length=10)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to='presence.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.CharField(max_length=50)),
                ('statistiques', models.TextField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapports', to='presence.etudiant')),
            ],
        ),
    ]
