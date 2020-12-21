# Generated by Django 3.1.4 on 2020-12-21 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ForestManagement', '0005_auto_20201221_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
