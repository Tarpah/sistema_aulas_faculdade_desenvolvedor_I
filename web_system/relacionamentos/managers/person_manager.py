from relacionamentos.managers import BaseManager


class PersonManager(BaseManager):

    def find_by_nome(self, nome: str) -> list['Person']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(name__icontains=
                                   nome).order_by('-name')[:2]
            return list(consulta)
        else:
            raise TypeError('O nome deve ser string e não pode estar vazia')