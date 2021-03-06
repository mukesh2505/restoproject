# Generated by Django 3.1.6 on 2021-02-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210219_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(default=None, max_length=50, null=True)),
                ('profile_pic', models.CharField(max_length=1000, null=True)),
                ('facebook_url', models.CharField(max_length=1000, null=True)),
                ('tweet_url', models.CharField(max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'our_team',
                'managed': True,
            },
        ),
    ]
