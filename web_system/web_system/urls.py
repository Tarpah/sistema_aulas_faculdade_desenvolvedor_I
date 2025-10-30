from django.contrib import admin
from django.urls import path, include
from web_system.views import index

urlpatterns = [
    path('', index, name='index'),
    path('relacionamentos/', include('relacionamentos.urls',  namespace="app"),),
    path('aula/', include('aula.urls'),),
    path('admin/', admin.site.urls),
]