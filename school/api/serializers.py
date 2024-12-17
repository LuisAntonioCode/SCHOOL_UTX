from rest_framework import serializers
from school.models import Cursos, Horarios, Generos, Estudiantes

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'

class HorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios
        fields = '__all__'

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        read_only_fields = ('fecha_registro',)