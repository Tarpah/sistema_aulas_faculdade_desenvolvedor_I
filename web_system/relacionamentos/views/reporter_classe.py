from symtable import Class

from django.shortcuts import render
from relacionamentos.models import Reporter
from django.views import View

class ReporterListClasse(View):

    @staticmethod
    def get(request):
        query_set_reporters = Reporter.objects.all()

        lista_reporters = {
            'lista': query_set_reporters,
        }

        return render(request, 'reporter/list.html', lista_reporters)

class ReportListDetailsClasse(View):

    @staticmethod
    def get(request, pk):
        reporter = Reporter.objects.get(id=pk)
        context = {
            'reporter': reporter,
        }
        return render(request, 'reporter/read.html', context)
