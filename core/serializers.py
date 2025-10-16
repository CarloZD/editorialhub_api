from rest_framework import serializers
from .models import Editorial, Libro

class LibroSerializer(serializers.ModelSerializer):
    editorial_nombre = serializers.CharField(source='editorial.nombre', read_only=True)

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'genero', 'anio', 'editorial', 'editorial_nombre']


class EditorialSerializer(serializers.ModelSerializer):
    libros = LibroSerializer(many=True, read_only=True)

    class Meta:
        model = Editorial
        fields = ['id', 'nombre', 'pais', 'libros']
