from .base_model import BaseModel
from django.db import models
from ..enumerate.genero import Genero

class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    genero = models.CharField(max_length=20,
                              choices=Genero,
                              default=Genero.NOT_SPECIFIED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
