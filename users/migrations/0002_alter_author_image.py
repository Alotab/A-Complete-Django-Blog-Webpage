# Generated by Django 4.1.1 on 2023-01-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
