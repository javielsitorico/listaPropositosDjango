from django.urls import include, path
from . import views

app_name = 'propositos'

urlpatterns = [
     path('', views.listaPropositos, name='listaPropositos'),
     path('crear/', views.crearProposito, name='crearProposito'),
     path('insertar/', views.insertarProposito, name='insertarProposito'),
     path('borrar/<int:idProposito>/', views.borrarProposito, name='borrarProposito'),
     path('modificar/<int:idProposito>/', views.modificarProposito, name='modificarProposito'),
     path('guardar/<int:idProposito>/', views.guardarProposito, name='guardarProposito'),
]
