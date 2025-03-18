from django.db import models
from django.utils import timezone as tz


# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()  # Campo email obrigatório
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=tz.now)
    mensagem = models.TextField(blank=True)  # Campo opcional
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    crm = models.CharField(max_length=7, blank=False)
    email = models.EmailField(blank=True)  
    data_cadastro = models.DateTimeField(default=tz.now)
    mensagem = models.TextField(blank=True)  
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)
    especialidades = models.ManyToManyField("Especialidade", related_name="medicos") 
    


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    def especialidades_display(self):
        # Retorna o nome da primeira especialidade associada, se houver
        especialidade = self.especialidades.first()
        return especialidade.nome if especialidade else "Sem especialidade"

