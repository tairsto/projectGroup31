# Generated by Django 5.0.3 on 2024-03-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_userscontacts_delete_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscontacts',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
