# Generated by Django 2.2.7 on 2019-12-02 09:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='face_codes',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=129, null=True), size=128), size=128),
        ),
    ]
