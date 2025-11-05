from aula.managers import BaseManager


class PerfilManager(BaseManager):

    def find_by_passaporte(self, passaporte: str) -> list['Perfil']:
        if isinstance(passaporte, str) and len(passaporte) > 0:
            consulta = self.filter(passaporte__icontains=passaporte).order_by('-passaporte')
            return consulta
            #return list(consulta)
        else:
            raise TypeError('O passaporte deve ser string e não pode estar vazia')