# Generated by Django 4.0.6 on 2022-07-17 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0016_product_price_stripe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_stripe',
        ),
    ]