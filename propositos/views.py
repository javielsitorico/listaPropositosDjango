from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .models import Proposito

from datetime import timedelta, date

# proximosPropositos devuelve los propositos a cumplir en 30 dias
def listaPropositos(request):
     
     propositos = Proposito.objects.all()
     contexto = {
          'propositos': propositos,
     }
     
     plantilla = loader.get_template('listaPropositos.html')
     
     return HttpResponse(plantilla.render(contexto, request))