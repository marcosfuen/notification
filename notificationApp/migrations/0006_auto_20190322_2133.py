# Generated by Django 2.1.7 on 2019-03-23 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notificationApp', '0005_registrationexternalities_revised'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationexternalities',
            options={'ordering': ['date'], 'verbose_name': 'incidencia', 'verbose_name_plural': 'incidencias'},
        ),
    ]