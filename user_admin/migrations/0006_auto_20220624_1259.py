# Generated by Django 3.1.7 on 2022-06-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0005_auto_20220624_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_bill_amt',
            field=models.IntegerField(default=0),
        ),
    ]
