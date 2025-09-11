from django.contrib import admin
from relacionamentos.models import Person, Reporter, Magazine, Article

admin.site.register((Person, Reporter, Magazine, Article))