# Generated by Django 5.0 on 2024-02-18 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PBFinance', '0002_alter_evenement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='text',
        ),
    ]
