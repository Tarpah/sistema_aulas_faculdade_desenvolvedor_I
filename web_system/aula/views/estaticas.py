from datetime import datetime
from django.http import HttpResponse


def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa noite"
    if 12 > agora.hour > 6:
        mensagem = "Bom dia"
    elif 0 < agora.hour <= 6:
        mensagem = "Boa madrugada"

    completo = f"<html> <body> <h1> {mensagem.capitalize()} visitante!" \
               f"<br />{agora}</h1> {request.META["REMOTE_ADDR"]} </body> </html>"
    return HttpResponse(completo)