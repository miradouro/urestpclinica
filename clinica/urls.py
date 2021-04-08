from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pacientes.api.viewsets import PacientesViewset
from agendamentos.api.viewsets import AgendamentosViewSet
from historicos.api.viewsets import HistoricosViewSet

route = routers.DefaultRouter()
route.register(r'pacientes', PacientesViewset, basename='pacientes')
route.register(r'agendamentos', AgendamentosViewSet, basename='agendamentos')
route.register(r'historicos', HistoricosViewSet, basename='historicos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
