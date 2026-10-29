from django import forms


class FileImportForm(forms.Form):
    file_source = forms.FileField()
