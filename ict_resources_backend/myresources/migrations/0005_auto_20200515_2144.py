# Generated by Django 3.0.5 on 2020-05-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0004_auto_20200515_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start',
            field=models.CharField(max_length=255),
        ),
    ]