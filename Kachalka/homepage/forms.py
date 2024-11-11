from django import forms
from .models import Records

class RecordsForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = '__all__'