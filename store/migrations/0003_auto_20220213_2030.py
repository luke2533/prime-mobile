# Generated by Django 3.2 on 2022-02-13 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_sim_free_screen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sim_free',
            new_name='SimFree',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='simfree',
            options={'verbose_name_plural': 'SIM Free'},
        ),
    ]
