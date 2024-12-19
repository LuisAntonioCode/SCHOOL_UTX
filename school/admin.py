from django.contrib import admin
from .models import Cursos, Horarios, Generos, Estudiantes

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Horarios)
class HorariosAdmin(admin.ModelAdmin):
    list_display = ('jornada',)

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ('genero',)

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'genero', 'correo', 'edad', 'telefono', 'curso', 'horario', 'activo', 'fecha_registro')
    readonly_fields = ('fecha_registro',)

#admin.site.register(Cursos)
#admin.site.register(Horarios)
#admin.site.register(Generos)
#admin.site.register(Estudiantes, EstudianteAdmin)
