# Generated by Django 4.0.5 on 2022-07-16 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0040_order_bill_status_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bill_receipt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cheque_image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='release_order',
        ),
    ]
