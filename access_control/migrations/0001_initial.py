# Generated by Django 5.1.4 on 2024-12-09 13:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_homepage', models.IntegerField(default=0)),
                ('view_about', models.IntegerField(default=0)),
                ('view_services', models.IntegerField(default=0)),
                ('view_suppliers', models.IntegerField(default=0)),
                ('view_employees', models.IntegerField(default=0)),
                ('view_salary', models.IntegerField(default=0)),
                ('view_reports', models.IntegerField(default=0)),
                ('view_access_system', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
