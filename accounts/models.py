from django.contrib.auth.models import User
from django.db import models

# Perfil de usuario general
class UserProfile(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('paciente', 'Paciente'),
        ('profesional', 'Profesional'),
    ]
    ESPECIALIDADES_CHOICES = [
        ('cardiologia', 'Cardiología'),
        ('dermatologia', 'Dermatología'),
        ('pediatria', 'Pediatría'),
        # Agrega otras especialidades aquí
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    tipo_usuario = models.CharField(max_length=19, choices=TIPO_USUARIO_CHOICES)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDADES_CHOICES, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)  # Opcional para ambos
    comuna = models.CharField(max_length=100, blank=True, null=True)  # Opcional para ambos
    
    def __str__(self):
        return f"{self.user.username} ({self.tipo_usuario})"
