# Generated by Django 4.2.4 on 2023-08-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='img',
            field=models.ImageField(upload_to='about_us/'),
        ),
        migrations.AlterField(
            model_name='emplayee',
            name='img',
            field=models.ImageField(upload_to='employee/'),
        ),
        migrations.AlterField(
            model_name='special',
            name='img',
            field=models.ImageField(upload_to='special/'),
        ),
    ]
