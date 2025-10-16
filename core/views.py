from rest_framework import viewsets, filters
from .models import Editorial, Libro
from .serializers import EditorialSerializer, LibroSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'genero']
