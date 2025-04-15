from django.shortcuts import render, redirect   
from sistema.forms import PacienteForm
from sistema.models import Paciente


def listarPacientes(request):
    pacientes = Paciente.objects.all()


    context = {
        'pacientes': pacientes, 

    }

    return render(
        request,
        'paciente/listar.html',
        context,
    )


def cadastroPacientes(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST, request.FILES )#request.FILES , só se tiver (imagens etc), request.POST pega tudo do resto(nome,email,cfp....)
        if form.is_valid():
            # se os dados forem válidos é salvo um novo paciente no Banco de Dados.
            form.save()
            return redirect('/pacientes')
        else:
            print("error no paciente_views.py - cadastroPacientes") 
    elif request.method == 'GET':
        form = PacienteForm()
    else: print("error no paciente_views.py - cadastroPacientes") 
    
    return render(
        request,
        'paciente/cadastro.html',
        {'form': form},
    )
