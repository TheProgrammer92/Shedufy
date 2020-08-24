# Generated by Django 3.0.5 on 2020-08-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresources', '0009_auto_20200813_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('etat', models.PositiveSmallIntegerField(choices=[(1, 'validé'), (2, 'annulté'), (4, 'refusé'), (3, 'en attente')], default=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
