# Generated by Django 5.1.6 on 2025-03-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/'),
        ),
    ]
