# Generated by Django 5.0.2 on 2024-03-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_website_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivateUser',
        ),
    ]