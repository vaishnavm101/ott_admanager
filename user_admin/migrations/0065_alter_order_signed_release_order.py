# Generated by Django 4.0.5 on 2022-08-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0064_order_b4_agency_discount_bill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='signed_release_order',
            field=models.FileField(blank=True, null=True, upload_to='signed-release-orders'),
        ),
    ]
