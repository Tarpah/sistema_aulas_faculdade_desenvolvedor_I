from django.db import models


class Operacoes(models.TextChoices):
    ADDITION = "+", "Adição"
    SUBTRACTION = "-", "Subtração"
    MULTIPLICATION = "*", "Multiplicação"
    DIVISION = "/", "Divisão"