# Generated by Django 5.0 on 2024-02-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBFinance', '0006_evenement_auteur_alter_evenement_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]