from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic.base import View
from .models import Serie, Episode

class IndexView( View ):

    def get ( self, request ):
        return render( request, 'index.html')

class SerieView( View ):

    def get( self, request ):

        # Si el usuario esta utenticado puede ver la vista
        if request.user.is_authenticated:

            username = request.user.username

            context = {
                'series': list( Serie.objects.all() ),
                'username': username
            }
            return render( request, 'series.html', context = context )
        
        # Si no delvolvera el error
        return render( request, 'noLogin.html')

class EpisodeView( View ):

    def get( self, request, serie_id: int ):

        if request.user.is_authenticated:

            context = {
                'episodes': list(Episode.objects.filter(serie_id=serie_id))
            }
            return render( request, 'episodes.html', context = context)
        
        return render( request, 'noLogin.html')