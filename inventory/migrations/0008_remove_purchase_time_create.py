# Generated by Django 4.0.4 on 2022-07-16 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_purchase_time_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='time_create',
        ),
    ]
