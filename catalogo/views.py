from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Pelicula, Director, Actor, Genero, Reseña, Favorito
from .serializers import *

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class ReseñaViewSet(viewsets.ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class BuscarPeliculasView(generics.ListAPIView):
    serializer_class = PeliculaSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        return Pelicula.objects.filter(titulo__icontains=query)
