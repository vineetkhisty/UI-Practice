# Generated by Django 4.0.4 on 2022-05-11 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='date',
            new_name='date1',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='password1',
        ),
    ]
