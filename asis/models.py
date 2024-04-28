
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

class Usuario(AbstractUser):
    DOCENTE = 'DOCENTE'
    FUNCIONARIO = 'FUNCIONARIO'
    
    TIPO_CHOICES = [
        (DOCENTE, 'Docente'),
        (FUNCIONARIO, 'Funcionario'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.username

    # Agregar related_name='usuarios' para evitar el conflicto de nombres
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='usuarios'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='usuarios'
    )

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cin = models.CharField(max_length=10)
    correo_institucional = models.EmailField()

class Funcionario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cin = models.CharField(max_length=10)
    correo_institucional = models.EmailField()
