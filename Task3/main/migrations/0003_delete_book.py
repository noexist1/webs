# Generated by Django 4.0.3 on 2022-04-22 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_alter_task_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]