# Generated by Django 2.2.4 on 2021-05-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_author_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books_authors_app.Author'),
        ),
    ]