from rest_framework import serializers
from ..models import Serie

#Utilizando solamente serializer
#class SerieSerializer( serializers.Serializer ):
    #id = serializers.IntegerField()
    #title = serializers.CharField()
    #description = serializers.CharField()

#Utilizando ModelSerializer
class SerieSerializer( serializers.ModelSerializer ):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Serie
        fields = '__all__'