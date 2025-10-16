from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo
