# Generated by Django 5.0.6 on 2024-05-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medmenwork_app', '0003_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='product_interest',
            field=models.CharField(choices=[('leather_ladies_hand_bag', 'Leather Ladies Hand Bag'), ('leather_hand_bags', 'Leather Hand Bags'), ('leather_laptop_bags', 'Leather Laptop Bags'), ('leather_backpack', 'Leather Backpack'), ('leather_wallet', 'Leather Wallet'), ('leather_accessories', 'Leather Accessories'), ('leather_home_decor', 'Leather Home Decor'), ('leather_jackets', 'Leather Jackets'), ('leather_watch_straps', 'Leather Watch Straps')], max_length=100),
        ),
    ]