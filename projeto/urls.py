from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def sobre(request):
    return HttpResponse("String")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre)
]
