from django.db import models

# Create your models here.
from django.utils import timezone

class Banner(models.Model):
    BANNER_TYPES = (
        ('home', 'Home'),
        ('about', 'About'),
        ('services', 'Services'),
        ('contact', 'Contact'),
        # Add more types as needed
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/banners/', default='media/banners/default.jpg')
    banner_type = models.CharField(max_length=50, choices=BANNER_TYPES)
    
    def __str__(self):
        return f"{self.title}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    contact = models.CharField(max_length=20, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class about(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.alt_text if self.alt_text else f"Slider Image {self.id}"

PRODUCT_CHOICES = [
    ('leather_ladies_hand_bag', 'Leather Ladies Hand Bag'),
    ('leather_hand_bags', 'Leather Hand Bags'),
    ('leather_laptop_bags', 'Leather Laptop Bags'),
    ('leather_backpack', 'Leather Backpack'),
    ('leather_wallet', 'Leather Wallet'),
    ('leather_accessories', 'Leather Accessories'),
    ('leather_home_decor', 'Leather Home Decor'),    
    ('leather_jackets', 'Leather Jackets'),
    ('leather_watch_straps', 'Leather Watch Straps'),
]

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    product_interest = models.CharField(max_length=100, choices=PRODUCT_CHOICES)
    enquiry = models.TextField()

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} - {self.product_interest}"



class LeatherProduct(models.Model):
    CATEGORY_CHOICES = [
        ('garments', 'Leather Garments'),
        ('bags', 'Leather Bags'),
        ('belts', 'Leather Belts'),
        ('small_goods', 'Small Leather Goods'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.get_category_display()
