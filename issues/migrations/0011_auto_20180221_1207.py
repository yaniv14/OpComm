# Generated by Django 2.0 on 2018-02-21 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0010_reference_referencerevision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='content',
            new_name='reference',
        ),
    ]
