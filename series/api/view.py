from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ViewSet
from ..models import Serie
from .serializers import SerieSerializer

"""class SerieApiView( APIView ):
    def get( self, request ):
        #Sin serializers
        #series = [serie.title for serie in Serie.objects.all()]

        series = SerieSerializer( Serie.objects.all(), many=True)
        #Valida que toda la indormacion sea correcta
        #series.is_valid(raise_exception=True)
        return Response(data=series.data, status=status.HTTP_200_OK)

    def post( self, request ):
        Serie.objects.create(title=request.POST['title'], description=request.POST['description'])
        return self.get(request)"""

#Utilizando los viewset - se tiene que crear un router
class SerieViewSet( ViewSet ):

    #Muestra un listado de series
    def list( self, request ):
        series = SerieSerializer( Serie.objects.all(), many=True)

        return Response(data=series.data, status=status.HTTP_200_OK)

    #Devuelve un valor en concreto
    def retrieve( self, request, pk: int ):
        serie = SerieSerializer( Serie.objects.get(pk=pk))

        return Response(data=serie.data, status=status.HTTP_200_OK)

    def create( self, request ):
        Serie.objects.create(title=request.POST['title'], description=request.POST['description'])
        return self.list(request)