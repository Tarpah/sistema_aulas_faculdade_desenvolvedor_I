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

class ReporterListDetailsClasse(View):

    @staticmethod
    def get(request, pk):
        reporter = Reporter.objects.get(id=pk)
        context = {
            'reporter': reporter,
        }
        return render(request, 'reporter/read.html', context)

class ReporterGerarCPF(View):

    @staticmethod
    def get(request, pk):
        objeto_reporter = get_object_or_404(Reporter, pk=pk)
        try:
            digitos = [str(random.randint(0, 9)) for _ in range(11)]
            cpf_formatado = (
                f"{digitos[0]}{digitos[1]}{digitos[2]}."
                f"{digitos[3]}{digitos[4]}{digitos[5]}."
                f"{digitos[6]}{digitos[7]}{digitos[8]}-"
                f"{digitos[9]}{digitos[10]}"
            )

            objeto_reporter.cpf = cpf_formatado
            objeto_reporter.save()

            return redirect('relacionamentos:gerar_cpf_classe')

        except:
            print("Erro gerando CPF")
            return redirect('relacionamentos:reporter_function_list')

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
            return redirect('relacionamentos:reporter_function_list')

        context = {
            'form': form
        }

        return render(request, 'relacionamentos/create_simple.html', context)