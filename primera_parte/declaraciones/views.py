from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ClienteForm

from declaraciones.models import Cliente, SolicitudServicio

# Create your views here.
def index(request):
    return HttpResponse("DECLARACIONES")  

def listar_clientes(request):
    clientes = Cliente.objects.all().values()
    #return JsonResponse(list(clientes), safe=False)
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, numero_identificacion):
    cliente = get_object_or_404(Cliente, numeroIdentificacion=numero_identificacion)
    solicitudes = SolicitudServicio.objects.filter(cliente=cliente)
    return render(request, 'detalle_cliente.html', {
        'cliente': cliente,
        'solicitudes': solicitudes
    })

def formulario_cliente(request):
    form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form})