from django import forms
from .models import Contact


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

class ContactForm(forms.ModelForm):
    product_interest = forms.ChoiceField(choices=PRODUCT_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Contact
        fields = [
            'full_name', 'company', 'phone_number',
            'email', 'website', 'product_interest', 'enquiry'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            'product_interest': forms.RadioSelect(choices=PRODUCT_CHOICES, attrs={'class': 'large_radio'}),

            # 'product_interest': forms.RadioSelect(choices=PRODUCT_CHOICES, attrs={'class': 'form-check-input'}),
            'enquiry': forms.Textarea(attrs={'placeholder': 'Your Enquiry', 'class': 'form-control'}),
        }



    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        if len(phone_number) < 10:
            raise forms.ValidationError("Phone number should have at least 10 digits.")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        # Check if email is in a valid format
        if '@' not in email:
            raise forms.ValidationError("Enter a valid email address with '@'.")
        return email
