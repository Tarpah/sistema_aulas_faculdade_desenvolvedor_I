import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from relacionamentos.forms import ReporterForm
from relacionamentos.models import Reporter
from django.views import View



class ReporterListView(View):
    login_url = reverse_lazy('account:login')
    permission_required = 'relacionamentos.view_reporter'

    @staticmethod
    def get(request):
        query_set_reporters = Reporter.objects.all()

        lista_reporters = {
            'lista': query_set_reporters,
        }

        return render(request, 'reporter/list.html', lista_reporters)

class ReporterDetailsView(PermissionRequiredMixin, View):
    login_url = reverse_lazy('account:login')
    permission_required = 'relacionamentos.view_reporter'


    @staticmethod
    def get(request, pk):
        objeto_reporter = Reporter.objects.get(id=pk)
        context = {
            'objeto_reporter': objeto_reporter,
        }
        return render(request, 'reporter/read.html', context)

class ReporterCPFGeneratorView(LoginRequiredMixin, PermissionRequiredMixin, View):

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
            return redirect('relacionamentos:reporter_list_class')

class ReporterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    @staticmethod
    def get(request, pk):
        objeto_reporter = get_object_or_404(Reporter, pk=pk)

        context = {
            'objeto_reporter': objeto_reporter,
        }

        return render(request, "reporter/delete.html", context)

    @staticmethod
    def post(request, pk):
        objeto_reporter = get_object_or_404(Reporter, pk=pk)

        try:
            v_reporter_id = request.POST.get("reporter_id", None)

            if int(v_reporter_id) == pk:
                objeto_reporter.delete()
                return redirect('relacionamentos:reporter_list_class')
            else:
                print('Recusou a deletar, pk do objeto não bate com o pk do POST')

        except Exception as e:
            print(e)
            context = {
                'objeto_reporter': objeto_reporter,
            }
            return render(request, "reporter/delete.html", context)
        return redirect('relacionamentos:reporter_list_class')

class ReporterCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
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
            return redirect('relacionamentos:reporter_list_class')

        context = {
            'form': form
        }
        return render(request, 'reporter/create_simple.html', context)

class ReporterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    @staticmethod
    def get(request, pk):
        objeto_reporter = get_object_or_404(Reporter, pk=pk)
        form = ReporterForm(instance=objeto_reporter)
        context = {
            'form': form,
            'objeto_reporter': objeto_reporter,
        }

        return render(request, 'reporter/update.html', context)

    @staticmethod
    def post(request, pk):
        objeto_reporter = get_object_or_404(Reporter, pk=pk)

        form = ReporterForm(request.POST, instance=objeto_reporter)

        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_list_class')

        context = {
            'form': form,
            'objeto_reporter': objeto_reporter,
        }
        return render(request, 'reporter/update.html', context)