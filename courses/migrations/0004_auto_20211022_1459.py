# Generated by Django 3.2.8 on 2021-10-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20211010_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='available_spaces',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='course_bookings',
            field=models.IntegerField(default=0),
        ),
    ]