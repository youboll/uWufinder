# Generated by Django 3.1.2 on 2020-10-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20201026_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Null', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Null', max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='acc_type',
            field=models.IntegerField(default=0),
        ),
    ]
