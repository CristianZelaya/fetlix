from django.urls import path, include
from .views import IndexView, SerieView, EpisodeView
#from .api.view import SerieApiView
from .api.router import router

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('series/', SerieView.as_view(), name='series'),
    path('episodes/<int:serie_id>', EpisodeView.as_view(), name='episodes'),
    #path('api/series/', SerieApiView.as_view())
    path('api/', include(router.urls)) #Rutas del viewset
]
