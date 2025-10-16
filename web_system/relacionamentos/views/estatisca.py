from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.core import serializers

from relacionamentos.models.reporter import Reporter

def calculos_basicos(request, x, y):
    soma = x+y
    subtracao = x-y
    divisao = x/y
    multiplicacao = x*y

    mensagem = (f'soma: {soma} </br>'
                f'subtracao: {subtracao} </br>'
                f'divisao: {divisao} </br>'
                f'multiplicacao: {multiplicacao}')

    return HttpResponse(mensagem)

def criptografia_senha(request, name):
    nome_original = name
    name_criptografado = ''
    for letra in name:
        if letra == 'A' or letra == 'a':
            name_criptografado += '4'

        elif letra == 'E' or letra == 'e':
            name_criptografado += '3'

        elif letra == 'I' or letra == 'i':
            name_criptografado += '1'

        elif letra == 'O' or letra == 'o':
            name_criptografado += '0'

        elif letra == 'U' or letra == 'u':
            name_criptografado += 'V'
        else:
            name_criptografado += letra

    resposta_final = (f'senha original: {nome_original} </br>' 
                      f'senha criptografada: {name_criptografado}')

    return HttpResponse(resposta_final)

def primeira_view(request):
    contexto = {
        'mensagem': 'Bom dia DEV I',
    }
    #mensagem = "Bom dia DEV I"
    #return HttpResponse(mensagem, status=200)
    return render(request, 'primeira.html', context=contexto)

def home_view(request):
    return render(request, 'home.html')

# exemplo do sor Model.objects.filter(xxx__icontains = name)
def nome(request, name): # serve para fazer chamadas como scripts ou models
    exemplo = Reporter.objects.find_by_nome(name)
    objeto = serializers.serialize('python', exemplo)
    return JsonResponse(objeto, safe=False)