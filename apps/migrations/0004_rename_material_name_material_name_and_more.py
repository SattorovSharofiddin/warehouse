# Generated by Django 5.0.3 on 2024-03-11 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_rename_product_qty_product_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='material_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
