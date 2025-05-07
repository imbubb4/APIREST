from django.contrib import admin
from .models import Director, Actor, Genero, Pelicula, Reseña, Favorito

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Reseña)
admin.site.register(Favorito)
