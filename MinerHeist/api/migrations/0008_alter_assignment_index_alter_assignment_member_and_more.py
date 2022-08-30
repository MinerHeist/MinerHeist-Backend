# Generated by Django 4.1 on 2022-08-30 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_assignment_found_alter_assignment_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedMember', to='api.member'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='s_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solvingMember', to='api.member'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='s_time',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url_slug',
            field=models.SlugField(blank=True, default='default-slug', max_length=64),
        ),
    ]
