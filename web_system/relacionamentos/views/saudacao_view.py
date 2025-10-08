from django.http import HttpResponse
from django.views import View
from datetime import datetime


class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = 'Boa noite'
        if 12 > agora.hour > 6:
            mensagem = 'Bom dia'
        elif 0 < agora.hour <= 6:
            mensagem = 'Boa madrugada'

        completo =  f'<html><body><h1>{mensagem.capitalize()}</h1> visitante</body>'+ \
                    f'<br />{agora}</h1><body></body></html>'
        return HttpResponse(completo)