# Generated by Django 3.2.7 on 2022-10-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumtek', '0004_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(default=False, max_length=400),
        ),
    ]
