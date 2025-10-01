from django.shortcuts import HttpResponse

def primeira_view(request):
    mensagem = "Bom dia DEV I"
    return HttpResponse(mensagem, status=200)