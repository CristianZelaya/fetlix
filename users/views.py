from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView( View ):

    #peticion get Muestra la vista html de login
    def get( self, request ):
        return render( request, 'login.html')

    #Peticion post para autentiarlos
    def post( self, request ):

        # utilizamos el metodo auth para autenticar el usuario nos regersa un usuario que coincida con la informacion que pasamos
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])

        #validamos que el usuario exista
        if user is not None:
            #funcion para el logeo de usuarios
            login(request, user)
            return HttpResponse( content=b'Success')
        return self.get( request )
