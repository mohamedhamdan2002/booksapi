# Generated by Django 4.1.1 on 2022-09-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0004_alter_books_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='photo_author',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='books',
            name='photo_book',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]