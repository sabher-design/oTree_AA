# Generated by Django 2.2.12 on 2024-03-21 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word_encryption_round2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='color',
        ),
    ]
