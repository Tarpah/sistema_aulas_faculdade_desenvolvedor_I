from django.contrib import admin
from django.urls import path, include
import relacionamentos.views as views_funcoes
from web_system.views import index

urlpatterns = [
    path('', index, name='index'),
    path('relacionamentos/', include('relacionamentos.urls'),),
    path('aula/', include('aula.urls'),),
    path('admin/', admin.site.urls),
]