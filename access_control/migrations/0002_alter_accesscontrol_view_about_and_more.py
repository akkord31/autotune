# Generated by Django 5.1.4 on 2024-12-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_about',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_access_system',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_employees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_homepage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_reports',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_services',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesscontrol',
            name='view_suppliers',
            field=models.IntegerField(),
        ),
    ]
