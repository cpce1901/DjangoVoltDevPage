# Generated by Django 5.1.3 on 2024-11-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_total_price_items_total_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='items',
            field=models.ManyToManyField(blank=True, to='api.items'),
        ),
    ]
