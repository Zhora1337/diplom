# Generated by Django 2.2.7 on 2019-12-06 11:09

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0016_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('route', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), size=None)),
                ('face_codes', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, default=0, null=True), blank=True, null=True, size=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
