# Generated by Django 3.2.7 on 2021-09-26 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0010_profile_participant_badges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='participant_badges',
        ),
        migrations.CreateModel(
            name='Badges_Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, default='', max_length=10000)),
                ('badge', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='root.badges')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
