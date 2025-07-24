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

class Declaracion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipoDeclaracion = models.CharField(max_length=50)
    añofiscal = models.IntegerField()
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    egresos = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('en_revision', 'En revisión'),
            ('enviada', 'Enviada'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente')
    