# Generated by Django 3.0.5 on 2020-08-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0003_auto_20200812_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='type',
        ),
        migrations.AddField(
            model_name='typeschedule',
            name='schedule',
            field=models.ManyToManyField(to='myresources.Schedule'),
        ),
        migrations.AlterField(
            model_name='typeschedule',
            name='type',
            field=models.CharField(choices=[('CC', 'CC'), ('SN', 'Session Normale'), ('COURS', 'COURS'), ('RATTRAPPAGE', 'RATTRAPPAGE'), ('TD', 'TD'), ('TP', 'TP')], default='COURS', max_length=20),
        ),
    ]
