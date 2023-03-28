from django import forms
from .models import table

class AddForm(forms.ModelForm):
    class Meta:
        model = table


        fields = ('fname','lname','phone','email','password','gender')

        widgets = {
            'fname':forms.TextInput (attrs={'class':'form-control'}),
            'lname':forms.TextInput (attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.TextInput (attrs={'class':'form-control'}),
            'password':forms.TextInput (attrs={'class':'form-control'}),
            'gender':forms.TextInput (attrs={'class':'form-control'})
        }