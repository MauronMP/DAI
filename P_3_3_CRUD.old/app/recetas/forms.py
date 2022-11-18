from django import forms

from .models import Receta

class PostForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = '__all__'