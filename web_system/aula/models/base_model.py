from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # atributos da minha classe
    class Meta:
        abstract = True # estou dizendo que ele não criará objeto com essa classe, logo será apenas usado como 'template'
        app_label = 'aula'