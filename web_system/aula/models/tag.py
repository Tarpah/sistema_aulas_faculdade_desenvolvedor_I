from .base_model import BaseModel
from django.db import models
from ..enumerate.genero import Genero
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.core.validators import MinLengthValidator
from ..validators import CodValidator
from ..validators import validate_par
from django.contrib import admin
import random
import string

class Tag(BaseModel):
    cod = models.CharField(max_length=10,
                           validators=[MinLengthValidator(10),
                           CodValidator("4444444444")],
                           blank=True)

    name = models.CharField(max_length=255, unique=True)
    genero = models.CharField(max_length=20,
                              choices=Genero,
                              default=Genero.NOT_SPECIFIED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TagAdmin(admin.ModelAdmin):
    list_display = ('cod','name','update_at')
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('update_at',)


def save(self, *args, **kargs): # esse código gera no campo 'cod' um valor aleatorio caso o campo fique vazio
    if self.cod is None or self.cod == '':
        letters = string.ascii_letters + string.digits
        self.cod = ''.join(random.choice(letters) for i in range(10))
    super().save(*args, **kargs)

def clean(self):
    # texto que já estava no código =  pode ser realizada aqui novas validações customizadas e
    if not isinstance(self.name, str):
        raise ValidationError({
            "name": 'Nome informado é do tipo errado'},
            code='error001')
    elif self.name == 'Teste':
        raise ValidationError(
            {"name":'Não é possivel salvar testes!'},
             code="error002")
    elif self.cod == "2222222222" and self.name == "IFRS Restinga":
        raise ValidationError(
            {"name": 'Combinação de nome e código errada',
            "cod":'Combinação de nome e código errada!'},
            code="error0101"
        )

