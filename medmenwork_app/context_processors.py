# If you don't have a context processor already, you can create one to provide the image data to the template.
# Create a new file named context_processors.py inside your app directory.

from django.conf import settings

def category_images(request):
    # Define your image URLs here
    category_images = {
        'Leather Garments': [
            'assets/Image/Rectangle 24.png',
            'assets/Image/Rectangle 24 (1).png',
            'assets/Image/Rectangle 24 (2).png',
            'assets/Image/Rectangle 24 (3).png',
            'assets/Image/Rectangle 24 (4).png',
            'assets/Image/Rectangle 24 (5).png'
        ],
        'Leather Bags': [
            'assets/Image/Rectangle 24.png',
            'assets/Image/Rectangle 24 (1).png',
            'assets/Image/Rectangle 24 (2).png',
            'assets/Image/Rectangle 24 (3).png',
            'assets/Image/Rectangle 24 (4).png',
            'assets/Image/Rectangle 24 (5).png'
        ],
        'Leather Belts': [
            'assets/Image/Rectangle 24.png',
            'assets/Image/Rectangle 24 (1).png',
            'assets/Image/Rectangle 24 (2).png',
            'assets/Image/Rectangle 24 (3).png',
            'assets/Image/Rectangle 24 (4).png',
            'assets/Image/Rectangle 24 (5).png'
        ],
        'Small Leather Goods': [
            'assets/Image/Rectangle 24.png',
            'assets/Image/Rectangle 24 (1).png',
            'assets/Image/Rectangle 24 (2).png',
            'assets/Image/Rectangle 24 (3).png',
            'assets/Image/Rectangle 24 (4).png',
            'assets/Image/Rectangle 24 (5).png'
        ],
    }
    return {'category_images': category_images}
