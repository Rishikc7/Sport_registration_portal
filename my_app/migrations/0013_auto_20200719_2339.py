# Generated by Django 3.0.3 on 2020-07-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_auto_20200718_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegemodel',
            name='number',
            field=models.IntegerField(help_text='Enter 10 digit mobile number', max_length=10),
        ),
    ]