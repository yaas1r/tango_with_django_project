from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>View about page</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>View index page</a>")
