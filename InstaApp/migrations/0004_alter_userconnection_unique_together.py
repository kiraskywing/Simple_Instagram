# Generated by Django 3.2.6 on 2021-08-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstaApp', '0003_post_posted_on'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userconnection',
            unique_together={('creator', 'following')},
        ),
    ]
