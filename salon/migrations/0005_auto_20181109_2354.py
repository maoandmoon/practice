# Generated by Django 2.1.2 on 2018-11-09 20:54

from django.db import migrations, models
import salon.validators


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20181108_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, validators=[salon.validators.validate_phone_number], verbose_name='Номер телефона'),
        ),
    ]
