# Generated by Django 5.0.3 on 2024-03-11 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_product_product_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_qty',
            new_name='qty',
        ),
    ]