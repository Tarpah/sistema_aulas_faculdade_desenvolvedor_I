from django.contrib import admin
from django.contrib.auth import authenticate
from django.urls import path, include
from web_system.views import index
from web_system import views
from .views import ContactView
from django.contrib.auth import views as auth_views
from web_system.forms.custom_login_form import CustomLoginForm
from .views import ProfileView

urlpatterns = [

    # rotas para logar
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name ="accounts/login.html",
        authentication_form=CustomLoginForm)),

    path('accounts/', include('django.contrib.auth.urls')),

    #rotas do contato
    path('classe/contato', ContactView.as_view(), name='class_contato'),
    path('funcao/contato', views.contact, name='function_contato'),
    #path('funcao/search/', views.busca, name='search_function'),


    path('', index, name='index'),
    path('relacionamentos/', include('relacionamentos.urls',  namespace="app"),),
    path('aula/', include('aula.urls'),),
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
]