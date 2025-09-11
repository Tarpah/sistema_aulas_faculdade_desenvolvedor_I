from django.core.exceptions import  ValidationError
from django.utils.translation import gettext_lazy as _


def _calcular_digito(digitos: str) -> str:
    pesos = range(len(digitos) +1, 1,-1)
    soma = sum(int(d) * p for d,p in zip(digitos,pesos))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)


def validate_cpf(valor : str) -> None:

    if len(valor) != 11:
        raise ValidationError(_("CPF deve conter 11 digito"),code='Invalid_length', params={'valor':valor},)

    if valor == valor[0] * 11:
        raise ValidationError(_('CPF invalido'),code='invalid', params={'valor':valor})

    d1 = _calcular_digito(valor[:9])
    d2 = _calcular_digito(valor[:10])

    if (valor[9] + valor[10] != (d1 + d2)):
        raise ValidationError(_('CPF invalido'), code='invalid', params={'valor':valor})