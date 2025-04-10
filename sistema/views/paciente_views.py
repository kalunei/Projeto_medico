from django.shortcuts import render
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
