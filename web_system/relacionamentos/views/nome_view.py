from django.http import HttpResponse
from django.views import View
from relacionamentos.models import Reporter


class NomeView(View):
    @staticmethod
    def get(request):
        objetos = Reporter.objects.all()
        mensagem = ''
        for objeto in objetos:
            mensagem += (f"id:{objeto.id} <br />"
                         f"nome:{objeto.name} <br />"
                         f"cpf:{objeto.cpf}<br />"
                         f"email:{objeto.email} <br />"
                         f"<hr>")
        return HttpResponse(mensagem, status=200)