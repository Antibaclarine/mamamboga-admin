# Generated by Django 4.2.1 on 2023-06-30 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rates',
            new_name='Rate',
        ),
    ]
