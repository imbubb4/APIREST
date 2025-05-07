from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('peliculas', PeliculaViewSet)
router.register('directores', DirectorViewSet)
router.register('actores', ActorViewSet)
router.register('generos', GeneroViewSet)
router.register('resenas', ReseñaViewSet)
router.register('favoritos', FavoritoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buscar/', BuscarPeliculasView.as_view()),
]
