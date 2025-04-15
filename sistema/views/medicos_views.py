from django.shortcuts import render, redirect   
from sistema.models import Medico
from sistema.forms import MedicoForm


def listarMedicos(request):
    medicos = Medico.objects.all()


    context = {
        'medicos': medicos,
    }

    return render(
        request,
        'medico/listar_medicos.html',
        context,
    )


def cadastroMedicos(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/medicos')
    else:
        form = MedicoForm()

    return render(
        request,
        'medico/cadastro.html',
        {'form':form},
    )