# Generated by Django 3.2 on 2022-03-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20220313_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='rating',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
