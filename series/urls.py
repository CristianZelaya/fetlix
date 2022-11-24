from django.urls import path
from .views import IndexView, SerieView, EpisodeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('series/', SerieView.as_view(), name='series'),
    path('episodes/<int:serie_id>', EpisodeView.as_view(), name='episodes')
]
