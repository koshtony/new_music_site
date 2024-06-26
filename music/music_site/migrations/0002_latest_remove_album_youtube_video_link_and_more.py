# Generated by Django 4.2.11 on 2024-05-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=1000, verbose_name='paste link of latest youtube video')),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='youtube_video_link',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='youtube_playlist_link',
        ),
        migrations.AddField(
            model_name='album',
            name='link',
            field=models.CharField(default='', max_length=1000, verbose_name='paste embed code for youtube album'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='playlist',
            field=models.CharField(default='', max_length=1000, verbose_name='paste embed code for youtube playlist'),
        ),
    ]
