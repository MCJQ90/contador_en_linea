from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from declaraciones.models import Cliente

# Create your views here.
def index(request):
    return HttpResponse("DECLARACIONES")  

def listar_clientes(request):
    clientes = Cliente.objects.all().values()
    #return JsonResponse(list(clientes), safe=False)
    return render(request, 'lista_clientes.html', {'clientes': clientes})