# Generated by Django 2.2.3 on 2019-07-04 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shot',
            old_name='type',
            new_name='session_type',
        ),
    ]
