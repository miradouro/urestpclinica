# Generated by Django 3.2 on 2021-04-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nasc', models.DateTimeField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=80, null=True)),
                ('num_endereco', models.IntegerField(blank=True, null=True)),
                ('bairro_endereco', models.CharField(blank=True, max_length=60, null=True)),
                ('cep', models.CharField(blank=True, max_length=100, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('rg', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pacientes',
                'managed': True,
            },
        ),
    ]