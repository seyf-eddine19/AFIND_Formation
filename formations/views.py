from django.shortcuts import render, redirect
from .models import Formation, Enrollment, FormationImage
from django.utils import timezone 


def home(request):
    content = {
        'formations' : Formation.objects.filter(status=True)
    }
    return render(request, 'index.html', content)

def formation_detail(request, pk):
    content = {
        'formation' : Formation.objects.get(id=pk),
        'formation_images' : FormationImage.objects.filter(formation=pk)
    }
    return render(request, 'formation_detail.html', content)

def enroll_form(request, pk):
    formation = Formation.objects.get(id=pk)
    content = {
        'formation' : formation
    } 
    
    if request.method == 'POST':
        formation_id = request.POST.get('formation')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        department = request.POST.get('department')
        academic_level = request.POST.get('academic_level')
        status = ''
        enrollment_date = timezone.now() 
        formation_id = formation.id 
        
        # Save the enrollment data to the database
        Enrollment.objects.create(
            formation_id=formation_id,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            department=department,
            academic_level=academic_level,
            status=status,
            enrollment_date=enrollment_date
        )
        
        # Redirect to a success page or another URL
        return redirect('/')  # Replace 'success' with the name of your success URL
    
    return render(request, 'enroll_form.html', content)
