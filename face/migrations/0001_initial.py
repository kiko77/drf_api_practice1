# Generated by Django 4.1.1 on 2022-10-16 09:04

from django.db import migrations, models
import face.models
import face.storage
import face.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='image')),
                ('media_filename', models.FileField(blank=True, null=True, storage=face.storage.OverwriteStorage(), upload_to=face.models.upload_location('image/'), validators=[face.validators.validate_image_size])),
                ('uid', models.TextField(blank=True)),
                ('upload_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='video')),
                ('media_filename', models.FileField(blank=True, null=True, storage=face.storage.OverwriteStorage(), upload_to=face.models.upload_location('video/'), validators=[face.validators.validate_video_size])),
                ('uid', models.TextField(blank=True)),
                ('upload_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]
