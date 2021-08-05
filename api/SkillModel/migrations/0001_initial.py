# Generated by Django 3.2.5 on 2021-08-02 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='cutting',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('collection', models.IntegerField()),
                ('lumbering', models.IntegerField()),
                ('exploitation', models.IntegerField()),
                ('prospecting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='farming',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('grain', models.IntegerField()),
                ('vegetables_fruit', models.IntegerField()),
                ('cash_crops', models.IntegerField()),
                ('reclaim', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='husbandry',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('hunt', models.IntegerField()),
                ('fowl', models.IntegerField()),
                ('livestock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='processing',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('smelt', models.IntegerField()),
                ('forge', models.IntegerField()),
                ('spin', models.IntegerField()),
                ('food_processing', models.IntegerField()),
                ('wood_stone_processing', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='social',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('eloquence', models.IntegerField()),
                ('communicate', models.IntegerField()),
                ('write', models.IntegerField()),
                ('manage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('land_transport', models.IntegerField()),
                ('water_transport', models.IntegerField()),
                ('fishing', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('cutting', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.cutting')),
                ('farming', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.farming')),
                ('husbandry', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.husbandry')),
                ('processing', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.processing')),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.social')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='SkillModel.vehicle')),
            ],
        ),
    ]