# Generated by Django 2.2.3 on 2019-07-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0002_auto_20190704_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shot',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddIndex(
            model_name='shot',
            index=models.Index(fields=['club'], name='shots_shot_club_51e387_idx'),
        ),
        migrations.AddIndex(
            model_name='shot',
            index=models.Index(fields=['timestamp'], name='shots_shot_timesta_d34c3c_idx'),
        ),
    ]
