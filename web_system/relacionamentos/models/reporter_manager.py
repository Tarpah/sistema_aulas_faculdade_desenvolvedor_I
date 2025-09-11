from datetime import date
from relacionamentos.models.base_manager import BaseManager
from django.db.models import QuerySet


class ReporterManager(BaseManager):
    def find_by_nome(self, nome:str) -> list['Reporter']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(name__icontains=
                                   nome).order_by('name')[:2]
            return list(consulta)
        else:
            raise TypeError('O nome deve ser string e não pode est ')

    def find_by_publication_date_since(self, publication_date: date)-> QuerySet['Reporter']:
        if isinstance(publication_date, date):
            today = date.today()
            consulta = self.filter(article__pub_date__range=(publication_date, today))
            return consulta
        else:
            raise TypeError("Você deve consultar com um objeto date")