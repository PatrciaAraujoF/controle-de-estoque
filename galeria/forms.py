from django import forms
from .models import Peca, DetalhesPeca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome']  
    def __init__(self, *args, **kwargs):
        super(PecaForm, self).__init__(*args, **kwargs)
       
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})

class DetalhesPecaForm(forms.ModelForm):
    class Meta:
        model = DetalhesPeca
        fields = ['peca', 'codigo', 'veiculo', 'modelo', 'quantidade_inicial', 'valor_unitario']
        widgets = {
            'peca': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'veiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if DetalhesPeca.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Este código já está em uso. Por favor, escolha outro.")
        return codigo
