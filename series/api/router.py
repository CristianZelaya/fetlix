from rest_framework.routers import DefaultRouter
from .view import SerieViewSet

router = DefaultRouter();

router.register(prefix='series', basename='series', viewset=SerieViewSet)