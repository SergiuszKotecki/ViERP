# Generated by Django 4.0.3 on 2022-04-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_seller_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbatch',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
