# Generated by Django 5.0.3 on 2024-03-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_usersrecycling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='bin_type',
            field=models.CharField(choices=[('כתום', 'כתום'), ('כחול', 'כחול'), ('חום', 'חום'), ('ירוק', 'ירוק'), ('סגול', 'סגול'), ('אפור', 'אפור'), ('מיחזורית- בקבוקי שתייה בנפח של מעל 1.5 ליטר ', 'מיחזורית- בקבוקי שתייה בנפח של מעל 1.5 ליטר '), ('קרטוניה', 'קרטוניה')], default=None, max_length=255, null=True),
        ),
    ]