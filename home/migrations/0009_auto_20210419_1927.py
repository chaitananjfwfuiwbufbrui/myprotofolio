# Generated by Django 3.0.8 on 2021-04-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210419_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_demo',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_gitlink',
            field=models.CharField(max_length=2000),
        ),
    ]