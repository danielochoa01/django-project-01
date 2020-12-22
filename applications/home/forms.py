from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo', 
            'subtitulo', 
            'cantidad'
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el Título'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el Subtítulo'
                }                
            ),
            'cantidad': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el Título'
                }

            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 10:
            raise(forms.ValidationError('Ingrese un número mayor a 10'))
        elif cantidad > 20:
            raise(forms.ValidationError('Ingrese un número menor a 20'))
        else:
            return cantidad