# Generated by Django 3.2 on 2021-05-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='book_photos'),
        ),
    ]
