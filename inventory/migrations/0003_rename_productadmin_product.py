# Generated by Django 4.2.1 on 2023-06-30 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_product_productadmin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAdmin',
            new_name='Product',
        ),
    ]
