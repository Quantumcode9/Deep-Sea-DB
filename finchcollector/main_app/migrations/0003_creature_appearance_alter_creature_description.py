# Generated by Django 5.0.1 on 2024-01-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_creature_family_creature_picture_creature_predators_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='appearance',
            field=models.CharField(default='default_value', max_length=200),
        ),
        migrations.AlterField(
            model_name='creature',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
