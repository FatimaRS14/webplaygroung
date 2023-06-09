from django import forms
from .models import Page #Se importa el modelo page para no iniciar el modelo desde 0

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}), #El placeholder nos servira pára qie el contenido que indicara se muestre dentro del campo y no fuera
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
        }
        labels = {
            'title':'', 'order':'', 'content': ''
        }