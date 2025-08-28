from django.db import models

class BaseModel(models.Model):

    # atributos da minha classe
    class Meta:
        abstract = True # estou dizendo que ele não criará objeto com essa classe, logo será apenas usado como 'template'
        app_label = 'aula'