# Generated by Django 3.1.4 on 2021-01-26 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(default='0', null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_quantity', models.IntegerField(default=0, null=True)),
                ('ordered_date', models.DateField(auto_now=True)),
                ('delivery_date', models.DateField()),
                ('price', models.IntegerField(default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForestManagement.product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_quantity', models.IntegerField(default=0, null=True)),
                ('ordered_date', models.DateField(auto_now=True)),
                ('delivery_date', models.DateField()),
                ('price', models.IntegerField(default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForestManagement.product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_quantity', models.IntegerField(default=0, null=True)),
                ('ordered_date', models.DateField(auto_now=True)),
                ('last_created_date', models.DateField(default='2000-1-1', null=True)),
                ('frequency', models.CharField(blank=True, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=50, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForestManagement.product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
