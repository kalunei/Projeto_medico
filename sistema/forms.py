from django import forms
from .models import Paciente
from .models import Medico

class PacienteForm(forms.ModelForm):
    class Meta: #class Meta server pra cfg o form
        model = Paciente #define qual o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'mensagem',]



class MedicoForm(forms.ModelForm):
    class Meta: #class Meta server pra cfg o form
        model = Medico #define qual o model que o form representa
        fields = ['nome', 'sobrenome', 'crm', 'mensagem', 'ativo',]