# Generated by Django 3.0.5 on 2020-05-21 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0011_auto_20200521_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='name',
            new_name='equipment',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='category',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='code_equipment',
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_equipment',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myresources.Equipment'),
            preserve_default=False,
        ),
    ]
