# Generated by Django 4.1 on 2022-08-30 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_member_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
    ]
