from rest_framework.viewsets import ModelViewSet
from .serializers import CursosSerializer, HorariosSerializer, GenerosSerializer, EstudiantesSerializer
from school.models import Cursos, Horarios, Generos, Estudiantes
from rest_framework import permissions


class CursosViewSet(ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
    permission_classes = [permissions.AllowAny]

class HorariosViewSet(ModelViewSet):
    queryset = Horarios.objects.all()   
    serializer_class = HorariosSerializer
    permission_classes = [permissions.AllowAny]

class GenerosViewSet(ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer
    permission_classes = [permissions.AllowAny]

class EstudiantesViewSet(ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
    permission_classes = [permissions.AllowAny]
