# Generated by Django 4.1.2 on 2022-10-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carcollection_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.URLField(default='https://random.com/image.png'),
            preserve_default=False,
        ),
    ]