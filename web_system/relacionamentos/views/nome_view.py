from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter


class NomeView(View):
    @staticmethod
    def get(request):
        exemplo = Reporter.objects.all()
        mensagem = ''
        for objeto in exemplo:
            mensagem += f"{objeto} <br />"
        return HttpResponse(mensagem, status=200)