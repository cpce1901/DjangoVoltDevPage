# Generated by Django 5.1.3 on 2024-11-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_budget_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='budgets/'),
        ),
    ]
