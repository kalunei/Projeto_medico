from django.urls import path
from sistema import views

app_name = 'sistema'
# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('', views.index, name='index'),
]

