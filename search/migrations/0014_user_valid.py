# Generated by Django 3.1.2 on 2020-11-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20201112_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
