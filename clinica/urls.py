from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from pacientes.api.viewsets import PacientesViewset
from agendamentos.api.viewsets import AgendamentosViewSet
from historicos.api.viewsets import HistoricosViewSet
from imagens.api.viewsets import ImagesHistoricoViewSet

route = routers.DefaultRouter()
route.register(r'pacientes', PacientesViewset)
route.register(r'agendamentos', AgendamentosViewSet)
route.register(r'historicos', HistoricosViewSet)
route.register(r'imagens_historicos', ImagesHistoricoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
