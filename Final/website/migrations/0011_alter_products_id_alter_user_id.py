# Generated by Django 5.0.2 on 2024-03-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_website_products_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
