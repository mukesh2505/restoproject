# Generated by Django 3.1.6 on 2021-02-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='full_name',
        ),
    ]
