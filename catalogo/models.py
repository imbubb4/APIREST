from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actores = models.ManyToManyField(Actor)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()

class Favorito(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)  # simulando nombre de usuario
