from django.http import HttpResponse
from django.views import View

class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = request.META['REMOTE_ADDR']
        return HttpResponse(mensagem, status=200)