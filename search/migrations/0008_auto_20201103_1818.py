# Generated by Django 3.1.2 on 2020-11-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20201101_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='acc_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='anime_mal_code',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default=None, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=15, unique=True),
        ),
    ]
