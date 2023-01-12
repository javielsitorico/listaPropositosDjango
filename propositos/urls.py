from django.urls import include, path
from . import views

urlpatterns = [
     path('', views.listaPropositos, name='listaPropositos'),
]
