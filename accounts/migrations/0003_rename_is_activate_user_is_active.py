# Generated by Django 4.1 on 2023-01-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]
