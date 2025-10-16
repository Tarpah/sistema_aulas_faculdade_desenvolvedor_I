from django.http import HttpResponse
from django.shortcuts import render
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

        completo = {'mensagem' : mensagem, 'horario': agora}


        return render(request, 'saudacao.html', context=completo)