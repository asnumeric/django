# Generated by Django 5.0 on 2024-01-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0019_rename_kilometrage_vehicule_duree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='duree',
            field=models.IntegerField(default=0),
        ),
    ]