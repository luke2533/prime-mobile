# Generated by Django 3.2 on 2022-03-25 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_phone_rating'),
        ('reviews', '0006_alter_phonereview_phone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonereview',
            name='phone_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.phone'),
        ),
    ]
