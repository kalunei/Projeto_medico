from django.urls import path
from sistema import views

app_name = 'sistema'
# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('', views.index, name='index'),
    #
    path('pacientes/', views.listarPacientes, name='listarPacientes'),
    path('pacientes/novo/', views.cadastroPacientes, name='criar_paciente'),
    path('pacientes/pefil/<int:paciente_id>', views.perfilPaciente, name='perfil_paciente'),
    #
    path('medicos/', views.listarMedicos, name='listarMedicos'),
    path('medicos/novo/', views.cadastroMedicos, name='criar_medico'),
    #
    path('login/', views.login, name='login'),
  
    
    
    
]

