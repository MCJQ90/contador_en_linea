from django.http import HttpResponse, JsonResponse

from declaraciones.models import Cliente

# Create your views here.
def index(request):
    return HttpResponse("DECLARACIONES")  

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return JsonResponse(listar_clientes(clientes), safe=False)
