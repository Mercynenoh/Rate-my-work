# Generated by Django 4.0.5 on 2022-06-13 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_alter_project_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='pic',
        ),
    ]
