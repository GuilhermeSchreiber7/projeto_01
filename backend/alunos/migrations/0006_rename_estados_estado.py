# Generated by Django 5.1.5 on 2025-02-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_alter_pessoa_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estados',
            new_name='Estado',
        ),
    ]
