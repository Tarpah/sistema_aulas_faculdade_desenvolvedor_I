from django import forms
from django.core.validators import MinLengthValidator


class ContactForm(forms.Form):
    subject = forms.CharField(label='Assunto',
                              max_length=100,
                              validators=[MinLengthValidator(3)],
                              help_text='Digite o assunto da mensagem'
                              )
    sender = forms.EmailField(label='E-mail',
                              help_text='Digite o seu endereço de e-mail principal',)
    message = forms.CharField(label='Mensagem',
                              help_text='Digite sua mensagem',
                              widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False,
                                   label='Deseja receber uma cópia?',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})
        self.fields.get('cc_myself').widget.attrs.pop('class')