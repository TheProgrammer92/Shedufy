# Generated by Django 3.0.5 on 2020-08-17 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0010_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='id_etat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myresources.Etat'),
        ),
    ]
