from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register
from .models import Serie, Episode

# Register your models here.
class SeriesAdmin( ModelAdmin ):
    pass

admin.site.register(Serie, SeriesAdmin)

#class EpisodeAdmin( ModelAdmin ):
    #pass

#con decoradores
@register( Episode )
class EpisodeAdmin( ModelAdmin ):
    pass

#admin.site.register(Episode, EpisodeAdmin)