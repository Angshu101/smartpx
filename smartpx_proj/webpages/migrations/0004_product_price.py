# Generated by Django 4.0.5 on 2022-07-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_remove_product_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=300, max_length=10),
            preserve_default=False,
        ),
    ]
