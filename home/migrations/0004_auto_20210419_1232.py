# Generated by Django 3.0.8 on 2021-04-19 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210419_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project_domain',
        ),
        migrations.AddField(
            model_name='domain',
            name='projecta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.projects'),
        ),
    ]