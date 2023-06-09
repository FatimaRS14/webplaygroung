from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm
# Create your views here.
class StaffRequiredMixin(object):
    #Este mixin requerira que el usuario sea miembro del staff
     #Se tiene que segui esta logica para controlar el metodo para controlar las peticiones y mantener el acceso en privado hasta que se inicie sesión
    #Servira como un filtro para comprobar si el usuario esta identificado
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


#Esta es una ListView
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm 
    success_url = reverse_lazy('pages:pages')
   
   
    #seccess_url = reverse{'pages:pages'} esto asi no se puede llamar y es su lugar se utilizara un metodo
    #que tiene la vista basada en clases llamado Get Success para retornar el nuevo valor
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form" #Esto es para hacer el cambio de formulario y que no se paresca al que ya se tenia 
    #success_url = reverse_lazy('pages:pages') Esto no se necesitara
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')