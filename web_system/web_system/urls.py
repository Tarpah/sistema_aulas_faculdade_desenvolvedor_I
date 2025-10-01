from django.contrib import admin
from django.urls import path, include
import relacionamentos.views as views_funcoes


urlpatterns = [
    path('relacionamentos/', include('relacionamentos.urls'),),
    path('admin/', admin.site.urls),
]

