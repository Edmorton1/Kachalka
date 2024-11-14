from django import forms
from .models import Records, Statistic

class RecordsForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = ('exercise', 'record', 'date')

class StatisticForm(forms.ModelForm):

    class Meta:
        model = Statistic
        fields = '__all__'

