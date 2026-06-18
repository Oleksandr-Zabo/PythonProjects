from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProjectForm(forms.ModelForm):
    description_source = forms.ChoiceField(
        choices=[("manual", "Ввести опис вручну"), ("markdown", "Підтягнути з README.md")],
        widget=forms.RadioSelect,
        initial="manual",
        label="Джерело опису"
    )
    markdown_file = forms.FileField(required=False, label="Файл README.md")

    class Meta:
        model = Project
        fields = ["title", "description", "image", "link", "description_source", "markdown_file"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        help_texts = {
            "description": "Можна залишити порожнім, якщо підтягуватимеш з README.md"
        }