# Generated by Django 3.1.7 on 2022-06-24 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0002_auto_20220624_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advt',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.order'),
        ),
    ]
