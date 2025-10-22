import random
import string

from django.shortcuts import render, get_object_or_404, redirect
from relacionamentos.models import Reporter


def reporter_list(request):
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
    exemplo = get_object_or_404(Reporter, pk=pk)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get("reporter_id", None)
            if int(v_reporter_id) == pk:
                exemplo.delete()
                return redirect('relacionamentos:exemplo_function_list')
        else:
            context = {
                'reporter': exemplo,
            }
            return render(request, 'reporter/delete.html', context)

    except Exception as e:
        context = {}
        print(e)
        return render(request, "reporter/list.html", context)

def gerar_cpf(request, pk):
    exemplo = get_object_or_404(Reporter, pk=pk)
    try:
        letras = string.ascii_letters + string.digits
        exemplo.cpf = ''.join(random.choice(letras) for i in range(10))
        exemplo.save()
        return redirect('relacionamentos:gerar_cpf')

    except:
        print("Erro gerando CPF")
        return redirect('relacionamentos:exemplo_function_list')