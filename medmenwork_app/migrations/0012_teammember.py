# Generated by Django 5.0.6 on 2024-05-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmenwork_app', '0011_settings_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team_images/')),
            ],
        ),
    ]
