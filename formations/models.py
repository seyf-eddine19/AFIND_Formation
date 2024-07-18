from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Formation(models.Model):
    title = models.CharField(max_length=200)
    session = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='formations/images/')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    discount = models.IntegerField(default=0, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Enter a discount percentage between 0 and 100")
    date = models.DateField(default=timezone.now, null=True)
    duration = models.CharField(max_length=100, null=True)
    instructor = models.CharField(max_length=560, default='', blank=True)
    department = models.CharField(max_length=255)
    places_left = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    place = models.CharField(max_length=255, default='')
    map_iframe = models.TextField(max_length=800, blank=True, null=True, help_text="iframe of the location on the map")
    status = models.BooleanField(default=True)
    
    class Meta:
        unique_together = [['title', 'session']]

    @property
    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return self.title


class FormationImage(models.Model):
    formation = models.ForeignKey(Formation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='formations/images/formation_%Y/')
    def __str__(self):
        return f"Image for {self.formation.title}"


class Enrollment(models.Model):
    # enrollment_id = models.AutoField(primary_key=True)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, default='')  
    region = models.TextField(blank=True, null=True) 
    specialty = models.CharField(max_length=255, default='', null=True)
    source = models.CharField(max_length=255, default='Manual', choices=[('Manual', 'Manual'), ('Facebook', 'Facebook'), ('Website', 'Website')], editable=False)
    status = models.CharField(max_length=255, default='Pending', choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')])
    enrollment_date = models.DateField(default=timezone.now, null=True)

    class Meta:
        unique_together = [['formation', 'phone']]

    @property
    def formation_title_session(self):
        return f"{self.formation.title} | {self.formation.session}"
    
    def __str__(self):
        return f"{self.full_name}"
    

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.email}"


class SiteContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('privacy_policy', 'Privacy Policy'),
        ('terms_of_service', 'Terms of Service'),
        ('faq', 'FAQ'),
    ]

    type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Content of the site section")

    def __str__(self):
        return self.get_type_display()


class SiteSettings(models.Model):
    SETTING_NAME_CHOICES = [
        ('EMAIL_RECEIVER', 'EMAIL RECEIVER'),
        ('EMAIL_HOST_PASSWORD', 'EMAIL HOST PASSWORD'),
        ('EMAIL_HOST_USER', 'EMAIL HOST USER'),
    ]
    setting_name = models.CharField(max_length=100, choices=SETTING_NAME_CHOICES, unique=True)
    setting_value = models.TextField(blank=True)

    def __str__(self):
        return self.setting_name