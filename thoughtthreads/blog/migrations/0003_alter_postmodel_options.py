# Generated by Django 5.1.3 on 2025-01-05 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_author_postmodel_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
