# Generated by Django 4.1.1 on 2023-01-24 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_author_remove_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]