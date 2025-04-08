from django.shortcuts import render
from sistema.models import Paciente
from sistema.models import Medico

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