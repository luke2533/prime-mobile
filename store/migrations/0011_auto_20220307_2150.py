# Generated by Django 3.2 on 2022-03-07 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220305_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price_1',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price_2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price_3',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price_4',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
        ),
        migrations.AlterField(
            model_name='phone',
            name='rating',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]