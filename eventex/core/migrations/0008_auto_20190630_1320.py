# Generated by Django 2.2.2 on 2019-06-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel('Course', 'CourseOld'),
    ]
