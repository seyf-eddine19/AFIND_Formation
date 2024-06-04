from django import forms
from .models import FormationImage


class FormationImageForm(forms.ModelForm):
    class Meta:
        model = FormationImage
        fields = ['image']
        

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
