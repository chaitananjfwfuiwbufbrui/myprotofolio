# Generated by Django 3.0.8 on 2021-04-19 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.domain'),
        ),
    ]
