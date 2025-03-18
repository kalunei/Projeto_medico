# Generated by Django 5.1.6 on 2025-03-11 18:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('criacao_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('mensagem', models.TextField(blank=True)),
                ('ativo', models.BooleanField(default=False)),
                ('imagem', models.ImageField(upload_to='img/%Y/%m/')),
            ],
        ),
    ]
