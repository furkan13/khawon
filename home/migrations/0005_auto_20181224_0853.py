# Generated by Django 2.1.4 on 2018-12-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181224_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media/logo'),
        ),
    ]
