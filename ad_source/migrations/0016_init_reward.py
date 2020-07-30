# Generated by Django 2.2.13 on 2020-07-30 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad_source', '0015_rename_related_names'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': ' Answer'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name_plural': '  Option'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': '   Question'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-reward_per_click'], 'verbose_name_plural': '    Task'},
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=18, max_digits=27)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='received_rewards', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='send_rewards', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rewards', to='ad_source.Task')),
            ],
            options={
                'unique_together': {('receiver', 'task')},
            },
        ),
    ]
