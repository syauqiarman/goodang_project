# Generated by Django 4.2.5 on 2023-09-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_name_item_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.CharField(default='', max_length=255),
        ),
    ]