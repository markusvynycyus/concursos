# Generated by Django 3.0.7 on 2020-06-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_banca', models.CharField(max_length=100, verbose_name='nome banca')),
                ('sigla_banca', models.CharField(max_length=50, verbose_name='sigla banca')),
            ],
        ),
    ]
