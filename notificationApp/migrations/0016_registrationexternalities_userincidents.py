# Generated by Django 2.1.7 on 2019-03-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificationApp', '0015_auto_20190322_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationexternalities',
            name='userIncidents',
            field=models.CharField(default='Usuario de la incidencia', max_length=250, verbose_name='Usuario'),
        ),
    ]
