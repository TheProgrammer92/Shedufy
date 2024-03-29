# Generated by Django 3.0.5 on 2020-08-05 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0002_auto_20200805_1714'),
        ('myresources_profil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codevalidation',
            name='id_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.Department'),
        ),
    ]
