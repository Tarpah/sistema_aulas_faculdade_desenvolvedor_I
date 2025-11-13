from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views import View
from relacionamentos.models import Reporter


class NomeView(View):
    @staticmethod
    def get(request, name=''):
        # padrão esperado http://localhost:8000/relacionamentos/exemplo/classe/%20?type=json ou http
        if name == '' or name == ' ':
            objetos = list(Reporter.objects.all())
            print('Lista')
        else:
            objetos = Reporter.objects.all()
            print('QuerySet')

        tipo = str(request.GET.get("type"))
        print('tipo:')
        print(tipo.lower())

        if tipo.lower() == 'http':
            print('entrou no http')
            mensagem = ''
            for objeto in objetos:
                mensagem += (f"id:{objeto.id} <br />"
                             f"nome:{objeto.name} <br />"
                             f"cpf:{objeto.cpf}<br />"
                             f"email:{objeto.email} <br />"
                             f"<hr>")

            return HttpResponse(mensagem, status=200)

        elif tipo.lower() == 'json':
            print('entrou no json')
            objeto = serializers.serialize('python', objetos)
            return JsonResponse(objeto, safe=False)
        else:
            print('entrou no else')
            return HttpResponse('BadRequest', status=400)


