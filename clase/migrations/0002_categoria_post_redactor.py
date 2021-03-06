# Generated by Django 4.0.3 on 2022-03-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('icono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subTitulo', models.CharField(max_length=150)),
                ('contenido', models.CharField(max_length=1500)),
                ('creacion', models.DateTimeField()),
                ('autor', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=30)),
                ('imagenDestacada', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Redactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=30)),
            ],
        ),
    ]
