# Generated by Django 3.0.8 on 2021-04-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210419_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='projects',
        ),
        migrations.AddField(
            model_name='projects',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.domain'),
        ),
    ]
