from django import forms
from .models import Snippet
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("title", "description", "code_block",
                  "language", "user", "tag",)
