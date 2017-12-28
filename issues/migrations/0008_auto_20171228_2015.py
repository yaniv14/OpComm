# Generated by Django 2.0 on 2017-12-28 18:15

import django.core.files.storage
from django.db import migrations, models
import issues.models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_proposalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueattachment',
            name='file',
            field=models.FileField(max_length=200, storage=django.core.files.storage.FileSystemStorage('/home/yaniv/projects/OpComm/uploads'), upload_to=issues.models.issue_attachment_path, verbose_name='File'),
        ),
    ]
