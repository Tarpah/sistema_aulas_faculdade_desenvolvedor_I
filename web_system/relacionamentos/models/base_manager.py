from django.db import models

class BaseManager(models.Manager):
    class Meta:
        app_label = 'relacionamentos'