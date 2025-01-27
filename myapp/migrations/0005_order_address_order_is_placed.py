# Generated by Django 5.1.3 on 2024-11-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='is_placed',
            field=models.BooleanField(default=0),
        ),
    ]
