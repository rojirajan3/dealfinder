# Generated by Django 4.1.7 on 2024-05-29 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0008_auto_20240529_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='UserId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.registerdb'),
        ),
    ]
