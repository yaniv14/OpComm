# Generated by Django 2.0.2 on 2018-03-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_unsubscribeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocuser',
            name='bio',
            field=models.CharField(blank=True, max_length=200, verbose_name='Bio'),
        ),
    ]
