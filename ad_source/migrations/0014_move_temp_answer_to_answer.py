# Generated by Django 2.2.13 on 2020-07-10 09:16

from django.db import migrations


class Migration(migrations.Migration):
    #  Renaming the 'ad_source_tempanswer' table while in a transaction is not supported
    #  on SQLite < 3.26 because it would break referential integrity.
    atomic = False

    dependencies = [
        ('ad_source', '0013_create_and_fill_temp_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answeredquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answeredquestion',
            name='selected_option',
        ),
        migrations.RemoveField(
            model_name='selectedoption',
            name='option',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='AnsweredQuestion',
        ),
        migrations.DeleteModel(
            name='SelectedOption',
        ),
        migrations.RenameModel(
            old_name='TempAnswer',
            new_name='Answer',
        ),
    ]
