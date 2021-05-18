# Generated by Django 3.2.3 on 2021-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associado',
            name='alergias_intolerancia',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='associado',
            name='endereco',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='associado',
            name='obs_gerais',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='associado',
            name='orientacao_alimentar',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='associado',
            name='saida',
            field=models.DateField(blank=True, default=None),
        ),
    ]
