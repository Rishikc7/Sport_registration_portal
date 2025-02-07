# Generated by Django 3.0.3 on 2020-07-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20200716_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegemodel',
            name='festName',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='registrationmodel',
            name='fest',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.CollegeModel', to_field='festName'),
        ),
    ]
