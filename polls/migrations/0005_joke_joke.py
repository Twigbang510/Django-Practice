# Generated by Django 4.1.7 on 2023-03-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20230323_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='joke',
            field=models.TextField(default=''),
        ),
    ]
