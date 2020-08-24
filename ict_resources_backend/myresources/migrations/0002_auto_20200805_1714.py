# Generated by Django 3.0.5 on 2020-08-05 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myresources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationequipment',
            name='id_equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.Equipment'),
        ),
        migrations.AddField(
            model_name='reservationschedule',
            name='id_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.Classe'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.Course'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myresources.Equipment'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
