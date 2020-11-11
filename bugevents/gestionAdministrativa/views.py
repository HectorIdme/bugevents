from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def loginView(request):
    return render(request, "gestionAdministrativa/templates/login.html")


def recuperarContraView(request):
    return render(request, "gestionAdministrativa/templates/recuperarContra.html")


class ControlAutenticacion(View):

    def get(self, request):
        loginView(request)

    def get(self, request):
        recuperarContraView(request)