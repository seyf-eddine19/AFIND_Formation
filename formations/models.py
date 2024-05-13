from django.db import models

# Instructors model
# class Instructor(models.Model):
#     full_name = models.CharField(max_length=255)
#     bio = models.TextField()
#     specialization = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20, blank=True, null=True) 
#     address = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.full_name}"

# Formation model
class Formation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='formations/images/')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    duration = models.CharField(max_length=100)
    instructor = models.CharField(max_length=560)
    department = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    enrollment_deadline = models.DateField()
    
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
    department = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    enrollment_date = models.DateField()

    class Meta:
        unique_together = [['formation', 'email']]


    def __str__(self):
        return f"{self.full_name} - {self.academic_level}"

