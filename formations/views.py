from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q 
from .models import Formation, Enrollment, FormationImage, ContactMessage


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
        'page': 'home'
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
        send_mail(
            subject,
            message,
            email,
            ['seyfeddine.tlm@gmail.com'],  # Replace with your email
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
        'page': 'formations'
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
        doctor_specialty = request.POST.get('doctor_specialty')
        address = request.POST.get('address')
        department = request.POST.get('department')
        academic_level = request.POST.get('academic_level')
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
                doctor_specialty=doctor_specialty,
                address=address,
                department=department,
                academic_level=academic_level,
                enrollment_date=enrollment_date
            )
            formation.places_left -= 1
            formation.save()
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
        # send_mail(
        #     subject,
        #     message,
        #     email,
        #     ['seyfeddine.tlm@gmail.com'],  # Replace with your email
        # )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html', content)


def faq(request):
    content = {}
    return render(request, 'faq.html', content)
    

def privacy_policy(request):
    content = {}
    return render(request, 'politique-de-confidentialite.html', content)
    

def terms_of_service(request):
    content = {}
    return render(request, 'conditions-generales-d-utilisation.html', content)
    

