# Generated by Django 5.0.3 on 2024-03-11 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_product_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='materials',
        ),
    ]
