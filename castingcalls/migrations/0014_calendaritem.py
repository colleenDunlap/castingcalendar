# Generated by Django 5.1.7 on 2025-05-01 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingcalls', '0013_alter_calendar_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=350)),
                ('is_complete', models.BooleanField(default=False)),
                ('casting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='castingcalls.casting')),
            ],
        ),
    ]
