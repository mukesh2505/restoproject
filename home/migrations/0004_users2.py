# Generated by Django 3.1.6 on 2021-02-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_users_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default=None, max_length=255)),
                ('full_name', models.CharField(default=None, max_length=255)),
                ('email', models.CharField(default=None, max_length=255)),
                ('mobile', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
            options={
                'db_table': 'users2',
                'managed': True,
            },
        ),
    ]