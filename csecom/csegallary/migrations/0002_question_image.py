# Generated by Django 4.0.3 on 2023-07-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csegallary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imges/'),
        ),
    ]
