# Generated by Django 4.1.7 on 2023-02-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('Sobrenome', models.CharField(max_length=100)),
                ('CPF', models.CharField(max_length=100)),
                ('mensagem', models.TextField(max_length=455)),
            ],
        ),
    ]
