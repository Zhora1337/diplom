# Generated by Django 2.2.7 on 2019-12-02 09:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20191202_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='face_codes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]