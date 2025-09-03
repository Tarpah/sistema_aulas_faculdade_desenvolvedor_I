# quem chama a função é o django, não nós, o @deconstructible explicita que essa classe pode ser destruida em tempo de execução.

@deconstructible
class CodValidator:

    def __init__(self, cod='0000000000'):
        self.cod = cod

    def __call__(self, valor):
        if valor == self.cod:
            raise ValidationError(
                _('Valor inválido'),
                params = {'valor': valor},
            )

    def __eq__(self, other):
        return (
            isinstance(other, CodValidator) # verifica o tipo de dado além do == que só verifica valores , tem relação direta com o deconstructible
            and self.code == other.code
        )
