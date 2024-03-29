# Generated by Django 3.0.5 on 2020-08-18 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0012_schedule_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeschedule',
            name='type_reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myresources.TypeSchedule'),
        ),
        migrations.AlterField(
            model_name='typeschedule',
            name='color',
            field=models.CharField(default='blue', max_length=255),
        ),
        migrations.AlterField(
            model_name='typeschedule',
            name='type',
            field=models.CharField(choices=[('CC', 'CC'), ('SN', 'Session Normale'), ('COURS', 'COURS'), ('RATTRAPPAGE', 'RATTRAPPAGE'), ('TD', 'TD'), ('TP', 'TP'), ('RESERVATION', 'RESERVATION')], default='COURS', max_length=20, unique=True),
        ),
    ]
