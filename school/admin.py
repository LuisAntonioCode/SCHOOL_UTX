from django.contrib import admin
from .models import Cursos, Horarios, Generos, Estudiantes

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin): 
    readonly_fields = ('fecha_registro',)

admin.site.register(Cursos)
admin.site.register(Horarios)
admin.site.register(Generos)
admin.site.register(Estudiantes, EstudianteAdmin)
