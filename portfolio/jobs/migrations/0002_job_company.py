# Generated by Django 4.0.4 on 2022-05-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
