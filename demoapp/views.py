from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello! This is index view I created for my demoapp.")