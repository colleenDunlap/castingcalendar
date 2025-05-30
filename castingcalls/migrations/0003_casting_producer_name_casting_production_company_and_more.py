# Generated by Django 5.1.7 on 2025-04-24 19:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingcalls', '0002_casting_is_published_casting_style_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='casting',
            name='producer_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='casting',
            name='production_company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='casting',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
