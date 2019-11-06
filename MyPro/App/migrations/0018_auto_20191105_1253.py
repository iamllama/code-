# Generated by Django 2.1.12 on 2019-11-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_passwordresethistory_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Organizatios',
                'verbose_name': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Roles',
                'verbose_name': 'Role',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='OrgName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]