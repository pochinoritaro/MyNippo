from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from account.models import User
from task.models import Task

class CreateTaskForm(ModelForm):
    reviewer = ModelMultipleChoiceField(
        queryset=User.objects.all().filter(is_superuser=False),
        widget=CheckboxSelectMultiple,
        label="レビュワー"
    )
    members = ModelMultipleChoiceField(
        queryset=User.objects.all().filter(is_superuser=False),
        widget=CheckboxSelectMultiple,
        label="メンバー"
    )

    class Meta:
        model = Task
        fields = ["title", "description", "document_url", "github_url", "is_public", "reviewer", "members"]
