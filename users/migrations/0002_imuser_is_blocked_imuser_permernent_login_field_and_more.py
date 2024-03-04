# Generated by Django 5.0.1 on 2024-03-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imuser',
            name='is_blocked',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='imuser',
            name='permernent_login_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imuser',
            name='temporal_login_field',
            field=models.IntegerField(default=0),
        ),
    ]