# Generated by Django 3.0.5 on 2020-08-22 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0023_auto_20200822_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='id_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.CategorieNotifications', to_field='type'),
        ),
    ]