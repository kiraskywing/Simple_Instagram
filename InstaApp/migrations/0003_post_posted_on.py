# Generated by Django 3.2.6 on 2021-08-10 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InstaApp', '0002_userconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]