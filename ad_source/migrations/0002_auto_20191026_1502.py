# Generated by Django 2.2.5 on 2019-10-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_source', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='result_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='result_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
