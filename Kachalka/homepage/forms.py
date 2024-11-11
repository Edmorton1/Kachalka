from django import forms
from .models import Records
import datetime

class RecordsForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = ('exercise', 'record', 'date')