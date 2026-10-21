from django import forms

from .models import UploadedFile

MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5 MB


class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('title', 'file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']

        if not file.name.lower().endswith('.csv'):
            raise forms.ValidationError('Please upload a .csv file.')

        if file.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError('File is too large. Max size is 5 MB.')

        return file
