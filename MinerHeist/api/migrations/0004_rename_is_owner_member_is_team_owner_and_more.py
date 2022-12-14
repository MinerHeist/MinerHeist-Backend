# Generated by Django 4.1 on 2022-08-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_member_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='is_owner',
            new_name='is_team_owner',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='f_name',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='l_name',
        ),
        migrations.RemoveField(
            model_name='puzzle',
            name='url',
        ),
        migrations.AddField(
            model_name='puzzle',
            name='url_slug',
            field=models.SlugField(default='default-slug', max_length=64),
        ),
    ]
