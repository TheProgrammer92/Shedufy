# Generated by Django 3.0.5 on 2020-08-22 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myresources', '0026_auto_20200822_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='is_valid',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresources.Classe'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresources.Course'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresources.Level'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresources.TypeSchedule', to_field='type'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_user_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
