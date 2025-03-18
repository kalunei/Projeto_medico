from django.contrib import admin

from sistema import models 
# Register your models here.


@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id','nome', 'email',)


@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):

    list_display=('id', 'nome',)


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nome', 'sobrenome','crm','email', 'data_cadastro','ativo','especialidades_display',)
    list_editable = ('ativo',)
    search_fields = ('id','nome', 'email',)

