# Generated by Django 4.0.1 on 2022-01-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
