# Generated by Django 3.2 on 2021-04-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_post_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]