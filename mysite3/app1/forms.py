from django import forms
from app1.models import Airport

class FormIn(forms.ModelForm):
    class Meta:
        model = Airport
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['to'].queryset = Airport.objects.all()
        self.fields['frm'].queryset = Airport.objects.all()
        
