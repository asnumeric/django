# Generated by Django 5.0.2 on 2024-02-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBFinance', '0011_alter_evenement_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]
