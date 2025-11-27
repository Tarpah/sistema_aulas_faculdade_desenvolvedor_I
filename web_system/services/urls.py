from django.urls import path
from rest_framework import routers
from .views import saudacao, ExemploSaudacao, api_root, calculo


app_name = 'services'

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [
    path('calculo', calculo, name="calculo"),
    path('', api_root, name="api-root"),
    path('saudacao/classe', ExemploSaudacao.as_view(), name="saudacao_classe"),
    path('saudacao', saudacao, name="saudacao"),
]