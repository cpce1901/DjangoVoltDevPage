# Generated by Django 5.1.3 on 2024-11-07 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_budget_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boss',
            options={'verbose_name': 'Mandante', 'verbose_name_plural': 'Mandantes'},
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materiales'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]
