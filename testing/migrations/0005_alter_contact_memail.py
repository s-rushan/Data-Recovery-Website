# Generated by Django 5.0.2 on 2024-02-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_rename_messsage_contact_des_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='memail',
            field=models.CharField(max_length=254),
        ),
    ]
