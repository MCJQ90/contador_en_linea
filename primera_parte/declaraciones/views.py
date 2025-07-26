from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ClienteForm
from django.http import HttpResponseRedirect

from declaraciones.models import Cliente, SolicitudServicio

# Create your views here.
def index(request):
    declaraciones = Cliente.objects.all()
    return render(request, 'index.html', {'declaraciones': declaraciones})

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
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/declaraciones/listar_clientes/")
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form})