from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator #Estas importaciones para la validacion de manesajes con usuarios 
from djago.http import Http404 #Herro generico para enviar si es que el usuario no le correponde el hilo que busca 


# Create your views here.
#Decorando el metódo
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"
    #model = Thread
    #ESTO NO SIRVE POR QUE Todo SE MANANDARA A TRAER DESDE LAS VISTAS


    #Filtrar instancias con query_set y en este se almacenaran los resultados
    #def get_queryset(self):
        #queryset = super(ThreadList, self).get_queryset()
        #return queryset.filter(users=self.request.user) #Se filtra por el usuario


#Mostrar mensajes a los que el usuario participa
@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread 
#Filtrar los hilos de los que el usuario solo forma parte

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404
        return obj
