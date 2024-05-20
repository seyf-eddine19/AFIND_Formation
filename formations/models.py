from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Formation model
class Formation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='formations/images/')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    duration = models.CharField(max_length=100)
    instructor = models.CharField(max_length=560, null=True)
    department = models.CharField(max_length=255)
    place = models.CharField(max_length=255, default='')
    discount = models.IntegerField(default=0, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Enter a discount percentage between 0 and 100")
    places_left = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    status = models.BooleanField(default=True)
    enrollment_deadline = models.DateField(default=timezone.now(), null=True)
    map_url = models.URLField(max_length=200, blank=True, null=True, help_text="URL of the location on the map")
    
    @property
    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return self.title


# Formation Image model
class FormationImage(models.Model):
    formation = models.ForeignKey(Formation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='formations/images/formation_%Y/')
    def __str__(self):
        return f"Image for {self.formation.title}"


# Enrollments model
class Enrollment(models.Model):
    # enrollment_id = models.AutoField(primary_key=True)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)  
    address = models.TextField(blank=True, null=True) 
    department = models.CharField(max_length=255, null=True)
    academic_level = models.CharField(max_length=100, null=True)
    doctor_specialty = models.CharField(max_length=255, default='', null=True)
    status = models.CharField(max_length=255, default='Pending', choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')])  # Updated field
    enrollment_date = models.DateField(default=timezone.now(), null=True)

    class Meta:
        unique_together = [['formation', 'email']]

    def __str__(self):
        return f"{self.full_name} - {self.academic_level}"
    

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.email}"
