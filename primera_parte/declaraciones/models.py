from django.utils import timezone
from django.db import models

# Create your models here.
class Cliente(models.Model):
    tipoIdentificacion = models.CharField(max_length=50)
    numeroIdentificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class SolicitudServicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipoServicio = models.CharField(max_length=50)
    añofiscal = models.IntegerField()
    fechaSolicitud = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=[('finalizada', 'Finalizada'), ('asistente_asignado', 'Asistente Asignado'), 
                                                      ('Pendiente', 'Pendiente'), ('en_proceso', 'En proceso')], default='Pendiente')
    observaciones = models.TextField(blank=True)

class AsistenteContable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo')

class AsignacionAsistente(models.Model):
    solicitudServicio = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    usuarioAsignado = models.ForeignKey(AsistenteContable, on_delete=models.CASCADE)
    fechaAsignacion = models.DateField(auto_now_add=True)

class Declaracion(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    tipoDeclaracion = models.CharField(max_length=50)
    añofiscal = models.IntegerField()
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    egresos = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[
        ('Pendiente', 'Pendiente'),
        ('en_revision', 'En revisión'),
        ('enviada', 'Enviada'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada')
    ], default='Pendiente')
    valorImpuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fechaPresentacion = models.DateField(null=True, blank=True)

