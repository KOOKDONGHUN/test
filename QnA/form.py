from django import forms
from QnA.models import Qpost

class QpostForm(forms.ModelForm):
    class Meta:
        model = Qpost
        fields = ('title','content',)