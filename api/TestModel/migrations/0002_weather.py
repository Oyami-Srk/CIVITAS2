# Generated by Django 3.2.5 on 2021-07-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('total_day', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('weather', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('rain_num', models.CharField(max_length=20)),
            ],
        ),
    ]
