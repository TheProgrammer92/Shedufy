# Generated by Django 3.0.5 on 2020-08-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0015_auto_20200818_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeschedule',
            name='type',
            field=models.IntegerField(choices=[(1, 'cours'), (2, 'cc'), (3, 'rattrapage'), (4, 'TD'), (5, 'sn'), (6, 'reservation')], default=1, unique=True),
        ),
    ]
