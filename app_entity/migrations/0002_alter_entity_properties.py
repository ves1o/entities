# Generated by Django 4.1.4 on 2022-12-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_entity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='properties',
            field=models.ManyToManyField(null=True, to='app_entity.property'),
        ),
    ]