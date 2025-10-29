import string
import random
from django.shortcuts import render, get_object_or_404, redirect
from relacionamentos.forms import ReporterForm
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

class ReportGerarCPF(View):

    @staticmethod
    def get(request, pk):
        exemplo = get_object_or_404(Reporter, pk=pk)
        try:
            letras = string.ascii_letters + string.digits
            exemplo.cpf = ''.join(random.choice(letras) for i in range(10))
            exemplo.save()
            return redirect('relacionamentos:gerar_cpf_classe')

        except:
            print("Erro gerando CPF")
            return redirect('relacionamentos:exemplo_function_list')

class ReporterDeleteView(View):

    @staticmethod
    def get(request, pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            context = {
                'reporter': reporter,
            }
            return render(request, 'reporter/delete.html', context)

        except Exception as e:
            context = {}
            print(e)
            return render(request, "relacionamentos:reporter_class_delete", context)

class ReporterCreateView(View):
    @staticmethod
    def get(request):
        form = ReporterForm()
        context = {
            'form': form
        }
        return render(request, 'reporter/create_simple.html', context)

    @staticmethod
    def post(request):
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:exemplo_function_list')

        context = {
            'form': form
        }

        return render(request, 'relacionamentos/create_simple.html', context)