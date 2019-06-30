# Generated by Django 2.2.2 on 2019-06-30 13:46

from django.db import migrations


def forward_course_abc_to_mti(apps, schema_editor):
    """
    ABC: Abstract based class.
    MTI: Multi table inheritance.
    For each ABC, create an instance of MTI with all attributes.
    Save MTI.
    Associate the speakers from ABC to the MTI.
    Delete ABC.
    """
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


def copy_src_to_dst(Source, Destionation):
    for src in Source.objects.all():
        dst = Destionation(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )
        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190630_1334'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti),
    ]
