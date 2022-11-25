from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout

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
            return redirect('series')
        return self.get( request )

#Controlador de la vista para cerrar sesion
class LogoutView( View ):
    def get( self, request ):
        #Preuntamos ue si el usuario esta logueado, si esta cierra sesion y lo redirige al login
        if request.user.is_authenticated:
            logout( request )
        return redirect('login')