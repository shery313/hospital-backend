# Generated by Django 5.1.1 on 2024-10-10 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wabma', '0002_alter_appointment_options_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='symptoms',
        ),
    ]
