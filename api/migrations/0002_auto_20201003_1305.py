# Generated by Django 3.1.1 on 2020-10-03 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('Add', models.CharField(blank=True, max_length=200, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='queue',
            name='queue_length',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='logdata_get',
            name='store_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.store'),
        ),
        migrations.AddField(
            model_name='logdata_put',
            name='store_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.store'),
        ),
        migrations.AddField(
            model_name='queue',
            name='queue',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.store'),
        ),
    ]
