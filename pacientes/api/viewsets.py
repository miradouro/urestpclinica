from rest_framework import viewsets
from pacientes.api.serializers import PacientesSerializer
from pacientes.models import Pacientes


class PacientesViewset(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

