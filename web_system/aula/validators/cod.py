# quem chama a função é o django, não nós, o @deconstructible explicita que essa classe pode ser destruida em tempo de execução.
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

@deconstructible
class CodValidator:
    def __init__(self, cod='0000000000'):
        self.cod = cod

    def __call__(self, valor):
        try:
            if valor == self.cod:
                raise ValidationError(
                    _('Valor inválido'),
                    params = {'valor': valor},
                )
        except ValueError:
            pass

    def __eq__(self, other):
        return (
            isinstance(other, CodValidator) # verifica o tipo de dado além do == que só verifica valores, tem relação direta com o deconstructible
            and self.code == other.code
        )
