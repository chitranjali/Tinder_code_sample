# Generated by Django 2.0.5 on 2018-07-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adults', '0004_auto_20180708_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='adult',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
