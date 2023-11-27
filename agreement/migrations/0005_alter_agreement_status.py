# Generated by Django 4.2.6 on 2023-10-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0004_alter_agreement_options_agreement_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='status',
            field=models.CharField(choices=[(1, '1 - New'), (2, '2 - Generated'), (3, '3 - Signed'), (4, '4 - Forwarded'), (5, '5 - Shipped'), (6, '6 - Delivery Confirmed')], default=(1, '1 - New'), max_length=30, null=True),
        ),
    ]
