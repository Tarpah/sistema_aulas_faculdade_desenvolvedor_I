from relacionamentos.forms import BaseForm
from relacionamentos.models import Reporter

class ReporterForm(BaseForm):
    class Meta:
        model = Reporter
        fields = '__all__'