# Generated by Django 4.2 on 2023-05-03 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fullname',
            new_name='name',
        ),
    ]
