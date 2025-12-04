from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.urls import path


def home(request):
    return JsonResponse({"status": "Django backend is running!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

