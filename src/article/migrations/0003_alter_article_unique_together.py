# Generated by Django 5.0.7 on 2024-07-30 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together={('title', 'author')},
        ),
    ]
