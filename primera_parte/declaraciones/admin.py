from django.contrib import admin

from .models import Cliente, SolicitudServicio, AsistenteContable, AsignacionAsistente, Declaracion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('tipoIdentificacion', 'numeroIdentificacion', 'nombre', 'apellido', 'email', 'telefono')

class SolicitudServicioAdmin(admin.ModelAdmin):
    exclude = ('fechaSolicitud',)
    list_display = ('cliente', 'tipoServicio', 'añofiscal', 'fechaSolicitud', 'estado')

class AsistenteContableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'especialidad', 'estado')

class AsignacionAsistenteAdmin(admin.ModelAdmin):
    list_display = ('solicitudServicio', 'usuarioAsignado', 'fechaAsignacion')

class DeclaracionAdmin(admin.ModelAdmin):
    list_display = ('solicitud', 'tipoDeclaracion', 'añofiscal', 'ingresos', 'egresos', 'estado', 'valorImpuesto', 'fechaPresentacion') 

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(SolicitudServicio, SolicitudServicioAdmin)
admin.site.register(AsistenteContable, AsistenteContableAdmin)
admin.site.register(AsignacionAsistente, AsignacionAsistenteAdmin)
admin.site.register(Declaracion, DeclaracionAdmin)
