# Generated by Django 3.0.7 on 2020-07-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaFormacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_area', models.CharField(max_length=50, verbose_name='Area de Formação')),
            ],
        ),
    ]
