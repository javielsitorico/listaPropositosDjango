from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.exceptions import ValidationError

from .models import Proposito

from datetime import timedelta, date, datetime

# proximosPropositos devuelve los propositos a cumplir en 30 dias
def listaPropositos(request):
     propositos = Proposito.objects.all()
     contexto = {
          'propositos': propositos,
     }
          
     return render(request, 'listaPropositos.html', contexto)

def crearProposito(request):
     return render(request, 'crearProposito.html')

def insertarProposito(request):
     if(
          request.POST['proposito'] == '' 
          or request.POST['fechaObjetivo'] == ''
          or request.POST['fechaObjetivo'] < date.today()
        ):
          return HttpResponseRedirect(reverse('propositos:crearProposito'))     
     
     try:
          Proposito(
               proposito = request.POST['proposito'], 
               fechaObjetivo = request.POST['fechaObjetivo'], 
               conseguido = False
               ).save()
     except(ValidationError):
          return HttpResponseRedirect(reverse('propositos:crearProposito'))     
     else:
          return HttpResponseRedirect(reverse('propositos:listaPropositos'))
     
def borrarProposito(request, idProposito):
     Proposito.objects.get(id=idProposito).delete()
     return HttpResponseRedirect(reverse('propositos:listaPropositos'))     
