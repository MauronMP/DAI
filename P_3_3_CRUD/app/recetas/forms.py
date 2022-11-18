from django import forms

from .models import Receta

class PostForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = ('nombre', 'preparacion', 'foto',)

        widgets = {
            'nombre':  forms.TextInput(attrs={'class': 'form-control'}),
            'preparacion':  forms.TextInput(attrs={'class': 'form-control'}),
            'foto':  forms.FileInput(attrs={'class': 'form-control','type': 'file'}),
        }