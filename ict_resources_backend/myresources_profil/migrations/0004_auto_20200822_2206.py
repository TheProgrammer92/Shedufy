# Generated by Django 3.0.5 on 2020-08-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresources_profil', '0003_auto_20200812_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (7, 'teacher'), (4, 'admin'), (5, 'super admin')], primary_key=True, serialize=False),
        ),
    ]
