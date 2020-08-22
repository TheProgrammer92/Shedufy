# Generated by Django 3.0.5 on 2020-08-21 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0021_categorienotifications_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorienotifications',
            name='value',
            field=models.CharField(default='cours', max_length=255),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='id_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresources.CategorieNotifications', to_field='type'),
        ),
    ]
