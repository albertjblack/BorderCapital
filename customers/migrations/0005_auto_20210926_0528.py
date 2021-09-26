# Generated by Django 3.2.7 on 2021-09-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
