# Django

# Comandos principais

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Parar criar um novo app -> python manage.py startapp sistema
7. Parar criar um superuser -> python manage.py createsuperuser
8. Para alterar a senha, caso você esqueça -> python manage.py changepassword nomedousuario
9- python -m pip install Pillow
10- python manage.py makemigrations
11- python manage.py migrate 
12- c

# PRINCIPAIS ARQUIVOS/PASTAS DO PROJECT
1. settings.py -> é o arquivo de configuração do projeto.
2. urls.py -> é o arquivo base [principal] de urls do projeto.


# DOCUMENTAÇÃO
1. `urls` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/ 
2. `settings` -> https://docs.djangoproject.com/en/5.1/topics/settings/ , https://docs.djangoproject.com/en/5.1/ref/settings/



# Criação das entidades do sistema
[PACIENTE]
nome 
sobrenome
email
telefone
criação
mensagem
ativo(s/n)
imagem

[MEDICO]
nome 
sobrenome
cmr 
email 
data cadastro do médico 
imagem
ativo
mensagem 

[CONSULTA]


[ENDEREÇO]


[ESPECIALIDADE]
ortopedia 
cardiologia
neurologia 
clinico geral




# Criar uma view qye vai rederizar um arquivo chamado seunome.html.
# No seunome.html coloque um h1 com o seu nome.
# Em seguida, crie uma url e chame esse aquivo seunome.html.



## Aula 08/04
1. injeção de contexto -> Utilizando o dicionário ``context`` para acessar todos os objetos.
- class Paciente (Modelo - Tabela)
- acessar todos os objetos(instâncias) que foram criadas a partir da class Paciente.
- Renderizar todos esses contatos no arquivo listar.html


## 1. Incluir alguns comando no settings.py para tratar as imagens
## 2. Ir no urls.py e incluir uma rota dinâmica para as imagens
## 3. Ir no listar.hrml e incluir o campo imagem; 