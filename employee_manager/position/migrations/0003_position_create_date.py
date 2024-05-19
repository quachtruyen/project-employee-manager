# Generated by Django 5.0.4 on 2024-05-14 17:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_remove_position_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]