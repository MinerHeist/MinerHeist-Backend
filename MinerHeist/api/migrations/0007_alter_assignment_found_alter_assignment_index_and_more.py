# Generated by Django 4.1 on 2022-08-22 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_assignment_s_time_alter_event_hint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='found',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='index',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='member',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedMember', to='api.member'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='s_member',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solvingMember', to='api.member'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
        migrations.AlterField(
            model_name='event',
            name='e_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='s_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
    ]
