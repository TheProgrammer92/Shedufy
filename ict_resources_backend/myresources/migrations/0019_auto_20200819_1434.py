# Generated by Django 3.0.5 on 2020-08-19 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0018_typeschedule_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='id_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.TypeSchedule', to_field='type'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='type_reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_reservation', to='myresources.TypeSchedule', to_field='type'),
        ),
    ]
