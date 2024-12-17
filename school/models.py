from django.db import models

# Create your models here.

# modelo de Cursos
class Cursos(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo de Horarios
class Horarios(models.Model):
    id = models.AutoField(primary_key=True)
    class Jornadas(models.TextChoices):
        MAÑANA = 'AM', 'Mañana'
        TARDE = 'PM', 'Tarde'
    jornada = models.CharField(max_length=2, choices=Jornadas.choices, default=Jornadas.MAÑANA, unique=True)
    
    def __str__(self):
        return self.jornada

# modelo de Generos    
class Generos(models.Model):
    id = models.AutoField(primary_key=True)
    class Generos(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
        OTRO = 'O', 'Otro'
    genero = models.CharField(max_length=1, choices=Generos.choices, default=Generos.MASCULINO, unique=True)
    
    def __str__(self):
        return self.genero

# modelo de Estudiantes
class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)
    edad = models.BigIntegerField()
    telefono = models.BigIntegerField(null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombres + ' ' + self.apellidos
