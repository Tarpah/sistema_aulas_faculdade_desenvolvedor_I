from django.shortcuts import render
from ..forms import ContactForm
from django.views import View

class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm()

        context = {
            'form': form,
            'url_form': 'class_contato',
        }
        return render(request, 'contact/page_contact.html', context)

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            cc_myself = form.cleaned_data.get('cc_myself')

            recipients = ['ricardo.santos@restinga.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)

            context = {
                'recipients': recipients,
                'form': form,
            }
            return render(request, 'contact/thanks.html', context)

        context = {'form': form,
                   'url_form': 'function_contato',
                   }
        return render(request, 'contact/page_contact.html', context)