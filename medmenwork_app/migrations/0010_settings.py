# Generated by Django 5.0.6 on 2024-05-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmenwork_app', '0009_delete_category_alter_leatherproduct_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('ig_link', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('copyright', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
