# Generated by Django 5.0.1 on 2024-02-12 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_cohort_cohortmember_imuser_delete_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='N/A', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='N/A', null=True)),
                ('start_date_and_time', models.DateTimeField()),
                ('is_repeated', models.BooleanField()),
                ('repeat_frequency', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('venue', models.CharField(max_length=100)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cohort')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_attendance_author', to='users.imuser')),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_assignee', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_author', to='users.imuser')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_submitter', to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='QueryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.imuser')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.query')),
            ],
        ),
    ]
