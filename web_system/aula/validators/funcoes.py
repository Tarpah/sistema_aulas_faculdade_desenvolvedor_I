from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# o valor nesse contexto é o campo lá no form.

def validate_par(valor):
    try:
        if int(valor) % 2 != 0:
            raise ValidationError(
                _("Não é um valor par"),
                params={"value": valor}, # a lógica de passar dados para o fluxo de dados é feito em params, é aqui que o django conversa com a próxima etapa do sistema.
            )
    except ValueError:
        pass

# '_' internacionalização