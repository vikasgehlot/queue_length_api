# Generated by Django 3.1.1 on 2020-10-03 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201003_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logdata_get',
            old_name='store_name',
            new_name='store',
        ),
        migrations.RenameField(
            model_name='logdata_put',
            old_name='store_name',
            new_name='store',
        ),
        migrations.RenameField(
            model_name='queue',
            old_name='queue',
            new_name='store',
        ),
    ]