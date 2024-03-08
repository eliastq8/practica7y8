from django.forms import ModelForm
from .models import Fruta

class Fruta(ModelForm):
    class Meta:
        model=Fruta
        fields=[
            'nombre',
            'color',
            'presentacion',
        ]