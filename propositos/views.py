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

def proximosPropositos(request):
     propositos = Proposito.objects.all()
     contexto = {
          'propositos': propositos,
     }
     return render(request, 'listaPropositosSimple.html', contexto)

def crearProposito(request):
     return render(request, 'crearProposito.html')

def insertarProposito(request):
     if(
          request.POST['proposito'] == '' 
          or request.POST['fechaObjetivo'] == ''
          or datetime.strptime(request.POST['fechaObjetivo'], '%Y-%m-%d').date() < date.today()
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

def modificarProposito(request, idProposito):
     proposito = Proposito.objects.get(id=idProposito)
     contexto = {
          'proposito': proposito,
     }
     
     return render(request, 'modificarProposito.html', contexto)

def guardarProposito(request, idProposito):
     if(
          request.POST['proposito'] == '' 
          or request.POST['fechaObjetivo'] == ''
          or datetime.strptime(request.POST['fechaObjetivo'], '%Y-%m-%d').date() < date.today()
        ):
          return HttpResponseRedirect(reverse('propositos:modificarProposito', args=(idProposito,)))     
     
     try:
          proposito = Proposito.objects.get(id=idProposito)
          proposito.proposito = request.POST['proposito']
          proposito.fechaObjetivo = request.POST['fechaObjetivo']
          proposito.save()
     except(ValidationError):
          return HttpResponseRedirect(reverse('propositos:modificarProposito', args=(idProposito,)))     
     else:
          return HttpResponseRedirect(reverse('propositos:listaPropositos'))

def completarProposito(request, idProposito):
     proposito = Proposito.objects.get(id=idProposito)
     proposito.conseguido = True
     proposito.fechaConseguido = date.today()
     proposito.save()
     return HttpResponseRedirect(reverse('propositos:listaPropositos'))

def resetearProposito(request, idProposito):
     proposito = Proposito.objects.get(id=idProposito)
     proposito.conseguido = False
     proposito.fechaConseguido = None
     proposito.save()
     return HttpResponseRedirect(reverse('propositos:listaPropositos'))

def retrasarProposito(request, idProposito):
     if(
          request.POST['cantidadDias'] == '' 
          or int(request.POST['cantidadDias']) <= 0
        ):
          return HttpResponseRedirect(reverse('propositos:listaPropositos'))
     
     proposito = Proposito.objects.get(id=idProposito)
     proposito.fechaObjetivo = proposito.fechaObjetivo + timedelta(days=int(request.POST['cantidadDias']))
     proposito.save()
     
     return HttpResponseRedirect(reverse('propositos:listaPropositos'))