import random
import string

from django.shortcuts import render, get_object_or_404, redirect

from relacionamentos.forms import ReporterForm
from relacionamentos.models import Reporter


def function_reporter_list(request):
    query_set_reporters = Reporter.objects.all()

    lista_reporters = {
        'lista': query_set_reporters,
    }

    return render(request, 'reporter/list.html', lista_reporters)

def reporter_list_details(request, pk):
    reporter = Reporter.objects.get(id=pk)
    context = {
        'reporter': reporter,
    }
    return render(request, 'reporter/read.html', context)

def delete(request, pk):
    objeto_reporter = get_object_or_404(Reporter, pk=pk)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get("reporter_id", None)
            if int(v_reporter_id) == pk:
                objeto_reporter.delete()
                return redirect('relacionamentos:reporter_function_list')
        else:
            context = {
                'reporter': objeto_reporter,
            }
            return render(request, 'reporter/delete.html', context)

    except Exception as e:
        context = {}
        print(e)
        return render(request, "reporter/list.html", context)

def gerar_cpf_function(request, pk):
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

        return redirect('relacionamentos:gerar_cpf_function')

    except:
        print("Erro gerando CPF")
        return redirect('relacionamentos:reporter_function_list')

def create(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_function_list')
    else:
        form = ReporterForm()
    context = {
        'form': form
    }
    return render(request, 'reporter/create_simple.html', context)

def update(request, pk):
    objeto_reporter = get_object_or_404(Reporter, pk=pk)
    if request.method == 'POST':
        form = ReporterForm(request.POST, instance=objeto_reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_function_list')
    else:
        form = ReporterForm(instance=objeto_reporter)
    context = {
        'form': form,
        'objeto_reporter': objeto_reporter,
    }
    return render(request, 'reporter/update.html', context)
