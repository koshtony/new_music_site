# Generated by Django 4.2.11 on 2024-05-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_site', '0005_alter_latest_link_alter_playlist_playlist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery_images')),
            ],
        ),
    ]
