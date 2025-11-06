from  django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})
            if len(new_field.errors.data) > 0:
                new_field.field.widget.attrs.update(
                    {"class": "form-control is-invalid"})