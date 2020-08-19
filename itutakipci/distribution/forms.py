from .models import Distribution
from django import forms
from .models import Distribution,Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment','anon']
