# Generated by Django 3.2.4 on 2021-09-18 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesModel', '0004_raw_materialdetail_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raw_materialDetail_3',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('r_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecipesModel.raw_material', verbose_name='食品')),
            ],
        ),
        migrations.DeleteModel(
            name='Raw_materialDetail_2',
        ),
    ]
