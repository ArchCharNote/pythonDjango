# Generated by Django 4.0 on 2021-12-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animals',
            name='food',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
