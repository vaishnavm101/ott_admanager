# Generated by Django 3.1.7 on 2022-06-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0014_advt_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mode_of_pay',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Upi', 'Upi'), ('Cheque', 'Cheque'), ('Net-Banking', 'Net Banking'), ('None', 'None')], default='None', max_length=100),
        ),
    ]