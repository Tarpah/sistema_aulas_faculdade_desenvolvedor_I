from django.db import models

from relacionamentos.models import BaseModel, Magazine, Person, Paper


class Publication(BaseModel):
    magazine = models.ForeignKey(Magazine, on_delete=models.RESTRICT)
    paper = models.ForeignKey(Paper, on_delete=models.RESTRICT)
    editor = models.ForeignKey(Person, on_delete=models.RESTRICT)
    date = models.DateField()
    obs = models.TextField()

    def __str__(self):
        return f'{self.magazine}: {self.paper} edited by {self.editor} at {self.date}'