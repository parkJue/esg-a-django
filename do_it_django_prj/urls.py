from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def root(request):
    return HttpResponse("Hello Django")

from blog import views

urlpatterns = [
    path('', root),
    path('blog/', views.index),
    path('admin/', admin.site.urls),
]
