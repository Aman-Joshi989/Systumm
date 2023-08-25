# Generated by Django 4.2.4 on 2023-08-25 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subtitles_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitle',
            name='id',
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='video',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='subtitles_app.video'),
        ),
    ]
