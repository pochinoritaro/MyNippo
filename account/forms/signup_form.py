from django.forms import ModelForm, PasswordInput
from account.models import User

class SignUpForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = PasswordInput()
    
    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password"]
        widgets = {
            "password": PasswordInput(attrs={"placeholder": "Enter your password"}),
        }
