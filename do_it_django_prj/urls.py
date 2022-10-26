from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def root(request):
    return HttpResponse("Hello Django")

urlpatterns = [
    path('', root),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
]
