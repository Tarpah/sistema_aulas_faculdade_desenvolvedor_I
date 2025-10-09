from django.template.defaultfilters import title

from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()


# Seus imports necessários
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from relacionamentos.models import Reporter, Article, Magazine
from datetime import date

User = get_user_model()
# User.objects.create_superuser('admin', 'admin@email.com', 'admin')


# Exemplo de consulta e de impressão do resultado
def listar_registros():
    exemplos = Reporter.objects.all()
    return exemplos



def main():
    try:
        reporter = Reporter(name='Fernando', cpf='18640053006', email='fernando@gmail.com')
        reporter.full_clean()
        reporter.save()

    except ValidationError as e:
        raise e

# main()

def consultar():
    from relacionamentos.models import Reporter
    lista_reporters = Reporter.objects.filter(name='Fernando')
    lista_reporters_exata = Reporter.objects.filter(name__exact='Fernando')

    for reporters in lista_reporters_exata:
        print(f'Nome do reporter:{reporters.name}  ID:{reporters.id}')

def __main__():
    flag = True
    while flag:
        print("\n== MENU ===")
        print("1. Criar um registro")
        print("2. Listar registros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar()

        if opcao == "2":
            listar_registros()

        elif opcao == "0":
            print("Saindo do script...")
            flag = False
    print("Fim do script.")


consultar()

print('teste')


if __name__ == "__main__":
    __main__()


