# Generated by Django 2.0 on 2017-12-06 12:47

from django.db import migrations, models
import django.db.models.deletion
import ocd.base_models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confidential', models.BooleanField(default=False, editable=False, verbose_name='Is Confidential')),
                ('background', ocd.base_models.HTMLField(blank=True, null=True, verbose_name='Background')),
                ('order', models.PositiveIntegerField(default=100, verbose_name='Order')),
                ('closed', models.BooleanField(default=True, verbose_name='Closed')),
            ],
            options={
                'verbose_name': 'Agenda Item',
                'verbose_name_plural': 'Agenda Items',
                'ordering': ('meeting__created_at', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=ocd.base_models.create_uid, max_length=24, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('held_at', models.DateTimeField(verbose_name='Held at')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('scheduled_at', models.DateTimeField(blank=True, null=True, verbose_name='Scheduled at')),
                ('location', models.CharField(blank=True, max_length=300, null=True, verbose_name='Location')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('guests', models.TextField(blank=True, help_text='Enter each guest in a separate line', null=True, verbose_name='Guests')),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
                'ordering': ('-held_at',),
            },
        ),
        migrations.CreateModel(
            name='MeetingExternalParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Meeting External Participant',
                'verbose_name_plural': 'Meeting External Participants',
            },
        ),
        migrations.CreateModel(
            name='MeetingParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinal', models.PositiveIntegerField()),
                ('display_name', models.CharField(max_length=200, verbose_name='Name')),
                ('default_group_name', models.CharField(blank=True, choices=[('member', 'member'), ('board', 'board'), ('secretary', 'secretary'), ('chairman', 'chairman')], max_length=50, null=True, verbose_name='Group')),
                ('is_absent', models.BooleanField(default=False, verbose_name='Is Absent')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participations', to='meetings.Meeting', verbose_name='Meeting')),
            ],
            options={
                'verbose_name': 'Meeting Participant',
                'verbose_name_plural': 'Meeting Participants',
            },
        ),
    ]
