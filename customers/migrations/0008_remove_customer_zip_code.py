# Generated by Django 3.2.7 on 2021-09-26 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_alter_customer_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='zip_code',
        ),
    ]
