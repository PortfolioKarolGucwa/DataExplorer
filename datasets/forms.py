from django import forms
from .models import uploaded_file

class uploaded_file_form(forms.ModelForm):
    class Meta:
        model = uploaded_file
        fields = ('title', 'file',)