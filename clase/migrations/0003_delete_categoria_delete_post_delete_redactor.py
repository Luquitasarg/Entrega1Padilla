# Generated by Django 4.0.3 on 2022-03-21 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_categoria_post_redactor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Redactor',
        ),
    ]
