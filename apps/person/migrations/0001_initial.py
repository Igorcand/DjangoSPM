# Generated by Django 4.1.3 on 2022-11-17 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=255)),
                ('tipo_pessoa', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=32, null=True)),
                ('informacoes_adicionais', models.CharField(blank=True, max_length=1055, null=True)),
                ('data_criacao', models.DateTimeField(editable=False)),
                ('data_edicao', models.DateTimeField()),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_fis_info', serialize=False, to='person.pessoa')),
                ('cpf', models.CharField(blank=True, max_length=32, null=True)),
                ('rg', models.CharField(blank=True, max_length=32, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_jur_info', serialize=False, to='person.pessoa')),
                ('cnpj', models.CharField(blank=True, max_length=32, null=True)),
                ('nome_fantasia', models.CharField(blank=True, max_length=255, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=32, null=True)),
                ('responsavel', models.CharField(blank=True, max_length=32, null=True)),
                ('suframa', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
    ]
