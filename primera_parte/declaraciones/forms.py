from . import models
from django.forms import ModelForm


class ClienteForm(ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['tipoIdentificacion', 'numeroIdentificacion', 'nombre', 'apellido', 'direccion', 'email', 'telefono']
        