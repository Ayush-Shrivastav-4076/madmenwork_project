# Generated by Django 5.0.6 on 2024-05-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmenwork_app', '0002_contact_alter_banner_id_alter_client_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
