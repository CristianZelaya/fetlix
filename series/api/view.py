from rest_framework.views import APIView, Response, status
from ..models import Serie
from .serializers import SerieSerializer

#Sin serializers
class SerieApiView( APIView ):
    def get( self, request ):
        #Sin serializers
        #series = [serie.title for serie in Serie.objects.all()]

        series = SerieSerializer( Serie.objects.all(), many=True)
        #Valida que toda la indormacion sea correcta
        #series.is_valid(raise_exception=True)
        return Response(data=series.data, status=status.HTTP_200_OK)

    def post( self, request ):
        Serie.objects.create(title=request.POST['title'], description=request.POST['description'])
        return self.get(request)