# Generated by Django 2.0.2 on 2018-04-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_emailpixeluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailpixeluser',
            name='subject',
            field=models.CharField(blank=True, max_length=100, verbose_name='Subject'),
        ),
    ]