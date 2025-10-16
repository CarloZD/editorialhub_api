from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EditorialViewSet, LibroViewSet

router = DefaultRouter()
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
