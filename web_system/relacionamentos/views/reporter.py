import random

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from relacionamentos.forms import ReporterForm
from relacionamentos.models import Reporter



@require_http_methods(["GET"])
def reporter_list_function(request):
    query_set_reporters = Reporter.objects.all()

    lista_reporters = {
        'lista': query_set_reporters,
    }

    return render(request, 'reporter/list.html', lista_reporters)

@permission_required('relacionamentos:view_reporter', raise_exception=True)
@require_http_methods(["GET"])
def reporter_list_details_function(request, pk):
    objeto_reporter = Reporter.objects.get(id=pk)
    context = {
        'objeto_reporter': objeto_reporter,
    }
    return render(request, 'reporter/read.html', context)

@login_required
@permission_required('relacionamentos:delete_reporter', raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_delete_function(request, pk):
    objeto_reporter = get_object_or_404(Reporter, pk=pk)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get("reporter_id", None)
            if int(v_reporter_id) == pk:
                objeto_reporter.delete()
                return redirect('relacionamentos:reporter_list_function')
        else:
            context = {
                'objeto_reporter': objeto_reporter,
            }
            return render(request, 'reporter/delete.html', context)

    except Exception as e:
        context = {}
        print(e)
        return render(request, "reporter/list.html", context)

@permission_required('relacionamentos:change_cpf_reporter', raise_exception=True)
@require_http_methods(["GET"]) #
def reporter_cpf_generator_function(request, pk):
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

        return redirect('relacionamentos:reporter_cpf_generator_function')

    except:
        print("Erro gerando CPF")
        return redirect('relacionamentos:reporter_list_function')

@permission_required('relacionamentos:change_reporter', raise_exception=True)
@login_required
@require_http_methods(["GET", "POST"])
def reporter_create_function(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_list_function')
    else:
        form = ReporterForm()
    context = {
        'form': form
    }
    return render(request, 'reporter/create_simple.html', context)

@permission_required('relacionamentos:change_reporter', raise_exception=True)
@login_required
@require_http_methods(["GET", "POST"])
def reporter_update_function(request, pk):
    objeto_reporter = get_object_or_404(Reporter, pk=pk)
    if request.method == 'POST':
        form = ReporterForm(request.POST, instance=objeto_reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_list_function')
    else:
        form = ReporterForm(instance=objeto_reporter)
    context = {
        'form': form,
        'objeto_reporter': objeto_reporter,
    }
    return render(request, 'reporter/update.html', context)
