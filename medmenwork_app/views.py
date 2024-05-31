
# medmenwork_app/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Banner,Service, Client, SliderImage,PRODUCT_CHOICES,TeamMember,Activity
from .forms import ContactForm
from django.contrib import messages 
from django.http import JsonResponse
from .models import LeatherProduct
from django.contrib import messages



def home(request):
    banner = Banner.objects.filter(banner_type="home")
    clients = Client.objects.all()
    slider_images = SliderImage.objects.all()
    category_choices =PRODUCT_CHOICES
    products = LeatherProduct.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # Redirect to the same page after form submission
    else:
        form = ContactForm()

    context = {
        'form': form,
        'banners': banner,
        'clients': clients,
        'slider_images': slider_images,
        'category_choices': category_choices,
        'products': products,
    }

    return render(request, 'home.html', context)



def about_us(request):
    banners = Banner.objects.filter(banner_type="about")
    clients = Client.objects.all()
    team_members = TeamMember.objects.all()
    activities = Activity.objects.all().order_by('-date')
    return render(request, 'about.html', {
        'banners': banners,
        'clients': clients,
        'team_members': team_members,
        'activities': activities,

        })   

def contact(request):
    banners = Banner.objects.filter(banner_type="contact")
    clients = Client.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Example: save form data to the database, send email, etc.
            form.save()  # Assuming your form is linked to a model
            messages.success(request, 'Your enquiry has been submitted successfully!')
            return redirect('contact')
        
    else:
        form = ContactForm()

    return render(request, 'contact.html',
         {
           'form': form,
           'banners': banners,
           'clients': clients,
                       
        })
    # return render(request, 'contact.html', {"banners": banners})

def services(request):
    banners = Banner.objects.filter(banner_type="services")
    services = Service.objects.all()
    clients = Client.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Example: save form data to the database, send email, etc.
            form.save()  # Assuming your form is linked to a model
            messages.success(request, 'Your enquiry has been submitted successfully!')
            return redirect('services')
        
    else:
        form = ContactForm()

    return render(request, 'services.html', {
        'banners': banners, 
        'services': services,
        'clients': clients,
        'form': form,
        })


