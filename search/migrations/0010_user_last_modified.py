# Generated by Django 3.1.2 on 2020-11-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_user_type_acc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_modified',
            field=models.DateField(default=None),
        ),
    ]
