# Generated by Django 4.2.4 on 2023-08-26 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='realese_date',
            new_name='release_date',
        ),
    ]