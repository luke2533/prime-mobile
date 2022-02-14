# Generated by Django 3.2 on 2022-02-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='freindly_name',
            new_name='friendly_name',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='cost',
            new_name='from_cost',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='img_1',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='img_2',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='img_3',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='os',
        ),
        migrations.RemoveField(
            model_name='simfree',
            name='screen',
        ),
        migrations.AddField(
            model_name='phone',
            name='camera',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='capacity',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category'),
        ),
        migrations.AddField(
            model_name='phone',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='phone',
            name='img_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='phone',
            name='os',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='screen',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
