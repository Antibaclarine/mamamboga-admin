# Generated by Django 4.2.1 on 2023-06-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]