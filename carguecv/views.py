from django.shortcuts import render
#se traen tablas de modelos
from .models import Area, carga_cv
#librerias
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

#Login requerido y roles
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def carguecv(request):
    return render(request, "carguecv.html")
def Detail(request):
    return render(request, "detail.html")

#Url para vista principal HOME
def home(request):
    print(request.POST)
    return render (request,"home.html")

#Clase para listar con autenticacion
class BadgetView(LoginRequiredMixin, ListView):
    template_name = 'carguecv/carguecv.html'
    model = carga_cv
    paginate_by = 10
    ordering =['cedula']

#Clase para crear
class CreateCV(LoginRequiredMixin, CreateView):
    model = carga_cv
    success_url = reverse_lazy('carguecv')
    fields = '__all__'

#Clase para actualizar datos
class BadgetUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.todoslospermisos'
    model = carga_cv
    success_url = reverse_lazy('carguecv')
    fields = '__all__'

#Clase para ver los detalles
class BadgetDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'users.todoslospermisos'
    model = carga_cv

    def get_success_url(self):
        return reverse('')

#Metodo de busqueda
@login_required
def searchCv(request):
    if request.method == 'POST':
        pattern = request.POST['search']
        carga= carga_cv.objects.filter(nombre=pattern)
    return render(request,'carguecv/carga_search.html',{'object_list':carga, 'search':pattern})
