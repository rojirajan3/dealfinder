# Generated by Django 3.2.16 on 2024-05-29 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_auto_20240529_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdb',
            old_name='user',
            new_name='id',
        ),
    ]
