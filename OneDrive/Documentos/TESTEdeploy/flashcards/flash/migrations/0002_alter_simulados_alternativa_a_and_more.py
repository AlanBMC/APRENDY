# Generated by Django 5.0.1 on 2024-03-17 23:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulados',
            name='alternativa_a',
            field=models.TextField(default='Essa alternativa esta vazia'),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='alternativa_b',
            field=models.TextField(default='Essa alternativa esta vazia'),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='alternativa_c',
            field=models.TextField(default='Essa alternativa esta vazia'),
        ),
        migrations.AlterField(
            model_name='simulados',
            name='alternativa_d',
            field=models.TextField(default='Essa alternativa esta vazia'),
        ),
        migrations.CreateModel(
            name='EstatisticasSimulado_compartilhada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_tentativa', models.DateTimeField(auto_now=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estatisticas_aluno', to=settings.AUTH_USER_MODEL)),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estatisticas_pagina', to='flash.pagina')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estatisticas_prof', to=settings.AUTH_USER_MODEL)),
                ('questoes_corretas', models.ManyToManyField(blank=True, related_name='respostas_corretas', to='flash.simulados')),
                ('questoes_erradas', models.ManyToManyField(blank=True, related_name='respostas_erradas', to='flash.simulados')),
            ],
        ),
    ]
