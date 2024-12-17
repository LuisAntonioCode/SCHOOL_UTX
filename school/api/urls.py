from rest_framework import routers
from .views import CursosViewSet, HorariosViewSet, GenerosViewSet, EstudiantesViewSet

router = routers.DefaultRouter()
router.register(r'cursos', CursosViewSet, 'cursos')
router.register(r'horarios', HorariosViewSet, 'horarios')
router.register(r'generos', GenerosViewSet, 'generos')
router.register(r'estudiantes', EstudiantesViewSet, 'estudiantes')  

urlpatterns = router.urls