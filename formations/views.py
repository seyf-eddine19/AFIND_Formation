from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q 
from .models import Formation, Enrollment, FormationImage, ContactMessage, SiteContent, SiteSettings

def send_custom_email(subject, message, email):
    # Fetch settings from the database
    try:
        email_settings = SiteSettings.objects.get(setting_name='EMAIL_HOST_USER')
        email_password_settings = SiteSettings.objects.get(setting_name='EMAIL_HOST_PASSWORD')
        email_receiver_settings = SiteSettings.objects.get(setting_name='EMAIL_RECEIVER')
        
        # Override the settings
        settings.EMAIL_HOST_USER = email_settings.setting_value
        settings.EMAIL_HOST_PASSWORD = email_password_settings.setting_value
        # Send the email
        send_mail(
            subject,
            message,
            email,
            [email_receiver_settings.setting_value],
        )
    except SiteSettings.DoesNotExist:
        # Handle case where the settings are not found
        pass


def home(request):
    query = request.GET.get('q') 
    if query:
        formations = Formation.objects.filter(
            Q(title__icontains=query) | 
            Q(instructor__icontains=query) |
            Q(department__icontains=query) |
            Q(place__icontains=query)
        )
    else:
        formations = Formation.objects.filter(status=True)

    content = {
        'formations': formations,
    }
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save message to database
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message,
        )
        
        # Send email
        send_custom_email(
            subject,
            message,
            email,
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/#contact')
    return render(request, 'index.html', content)


def formations(request):
    query = request.GET.get('q') 
    if query:
        formations = Formation.objects.filter(
            Q(title__icontains=query) | 
            Q(instructor__icontains=query) |
            Q(department__icontains=query) |
            Q(place__icontains=query)
        )
    else:
        formations = Formation.objects.filter(status=True)
        
    content = {
        'formations': formations,
    }
    return render(request, 'formations.html', content)
    

def formation_detail(request, pk):
    formation = get_object_or_404(Formation, id=pk)
    formation_images = FormationImage.objects.filter(formation=pk)
    formations = Formation.objects.filter(status=True)[:4]
    content = {
        'formation': formation,
        'formation_images': formation_images,
        'formations' : formations
    }
    if request.method == 'POST':
        formation_id = formation.id
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        specialty = request.POST.get('specialty')
        
        enrollment_date = timezone.now()
        
        # Check if the user is already enrolled
        if Enrollment.objects.filter(formation_id=formation_id, email=email).exists():
            messages.error(request, 'You are already enrolled in this formation.')
        else:
            # Save the enrollment data to the database
            Enrollment.objects.create(
                formation_id=formation_id,
                full_name=full_name,
                email=email,
                phone=phone,
                region=region,
                specialty=specialty,
                source = 'Website',
                enrollment_date=enrollment_date
            )
            # formation.places_left -= 1
            # formation.save()
            try:
                # Send email
                send_custom_email(
                    f'{full_name} enrolled in {formation.title} formation',
                    f'{full_name} enrolled in {formation.title} formation by {email}',
                    email,
                )
                messages.success(request, 'successfully!')
            except:
                messages.error(request, 'successfully!')
                
            messages.success(request, 'Your form has been submitted successfully!')
            # return redirect('/')
    return render(request, 'formation_detail.html', content)


def about(request):
    content = {}
    return render(request, 'about.html', content)
    

def contact(request):
    content = {}
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save message to database
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message,
        )
        
        # Send email
        send_mail(
            subject,
            message,
            email,
            ['seyfeddine.tlm@gmail.com'],  # Replace with your email
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html', content)


def faq(request):
    # faqs = SiteContent.objects.filter(type='faq')
    content = {
        'faq': get_object_or_404(SiteContent, type='faq')
    }
    return render(request, 'faq.html', content)
    

def privacy_policy(request):
    content = {
        'policy': get_object_or_404(SiteContent, type='privacy_policy')
    }
    return render(request, 'politique-de-confidentialite.html', content)
    

def terms_of_service(request):
    content = {
        'terms': get_object_or_404(SiteContent, type='terms_of_service')
    }
    return render(request, 'conditions-generales-d-utilisation.html', content)
    