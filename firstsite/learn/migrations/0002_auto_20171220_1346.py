# Generated by Django 2.0 on 2017-12-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resuser',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
