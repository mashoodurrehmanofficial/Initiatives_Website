# Generated by Django 3.2.4 on 2021-08-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20210830_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reset_code',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
    ]
