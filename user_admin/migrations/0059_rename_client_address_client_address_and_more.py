# Generated by Django 4.0.5 on 2022-07-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0058_remove_client_is_agency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_company_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_gst_number',
            new_name='gst_number',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_mobile_no',
            new_name='mobile_no',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_taluka',
            new_name='taluka',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_whatsapp_mobile_no',
            new_name='whatsapp_mobile_no',
        ),
    ]