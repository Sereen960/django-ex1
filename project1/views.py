from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> home page</h1>")
def about(request):
    return HttpResponse("<h1> about page</h1>")
    