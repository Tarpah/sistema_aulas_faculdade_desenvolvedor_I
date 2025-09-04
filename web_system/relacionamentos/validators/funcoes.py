from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Cálculo dos dígitos verificadores do cpf método privado
def _calcular_digito(digits: str) -> str:
    pesos = range(len(digits) + 1, 1, -1) # pesos regressivos
    soma = sum(int(d) * p for d, p, in zip(digits, pesos))
    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)


def validate_cpf(valor : str) -> None:
    # tamanho
    if len(valor) !=11:
        raise ValidationError(_("CPF deve conter 11 dígitos."),
                              code="invalid_length",
                              params={"valor":valor},)

    # numeros repetidos
    if valor == valor[0] * 11:
        raise ValidationError(_("CPF inválido."),
                              code="invalid",
                              params={"valor": valor},)
    d1 = _calcular_digito(valor[:9])
    d2 = _calcular_digito(valor[:10])

    if (valor[9] + valor[10]) != (d1 + d2):
        raise ValidationError (_("CPF inválido."),
                               code="invalid",
                               params={"valor": valor},)