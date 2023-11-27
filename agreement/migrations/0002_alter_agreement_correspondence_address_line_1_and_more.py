# Generated by Django 4.2.6 on 2023-10-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='correspondence_address_line_1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='correspondence_address_line_2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='correspondence_city',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='correspondence_country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='correspondence_zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='email_2',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='phone_no_2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='shipping_address_line_1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='shipping_address_line_2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='shipping_country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='shipping_zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
