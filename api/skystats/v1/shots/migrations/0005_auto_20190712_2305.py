# Generated by Django 2.2.3 on 2019-07-12 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0004_auto_20190704_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('session_type', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterModelOptions(
            name='shot',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='shot',
            name='shots_shot_timesta_d34c3c_idx',
        ),
        migrations.RemoveField(
            model_name='shot',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shot',
            name='session_type',
        ),
        migrations.RemoveField(
            model_name='shot',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='shot',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shots.Session'),
            preserve_default=False,
        ),
    ]