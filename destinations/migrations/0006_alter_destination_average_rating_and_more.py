# Generated by Django 5.0.7 on 2024-09-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0005_alter_destination_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='average_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='destination',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
