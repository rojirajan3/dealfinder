# Generated by Django 4.1.7 on 2024-05-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0012_alter_selldb_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='UserId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Frontend.registerdb'),
        ),
    ]
