from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def saludo(request):
    return render(request, "/ambiente/ambiente.html")


class GreetingView(View):
    greeting = "Good day"

    def get(self, request):
        return HttpResponse(self.greeting)






