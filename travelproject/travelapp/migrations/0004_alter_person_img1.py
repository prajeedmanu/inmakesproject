# Generated by Django 3.2.8 on 2021-10-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_auto_20211031_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img1',
            field=models.ImageField(upload_to='inmakesproject'),
        ),
    ]