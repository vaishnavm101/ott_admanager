# Generated by Django 4.0.5 on 2022-07-29 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0057_alter_agency_marketer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_agency',
        ),
    ]