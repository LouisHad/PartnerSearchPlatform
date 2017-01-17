from django import forms

from PartnerSearch.models import Institution


class InstForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ('country',)

class TestForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100 )
