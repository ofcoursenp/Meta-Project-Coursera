# Generated by Django 4.1.2 on 2023-02-02 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookings',
            new_name='Booking',
        ),
    ]
