# Generated by Django 5.0 on 2023-12-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiqa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albom',
            name='rasm',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]