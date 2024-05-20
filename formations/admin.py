from django.contrib import admin
from .models import Formation, Enrollment, FormationImage, ContactMessage
from .admin_actions import export_as_csv

class FormationImageInline(admin.TabularInline):
    model = FormationImage
    extra = 1


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'department', 'enrollment_deadline', 'status')
    search_fields = ('title', 'department')
    list_filter = ('department', 'instructor')
    
    inlines = [FormationImageInline]

    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'get_formation_name', 'department', 'academic_level', 'enrollment_date', 'status')
    search_fields = ('full_name', 'phone', 'specialization')

    list_filter = ('department', 'formation__title')
    actions = [export_as_csv]
    def get_formation_name(self, obj):
        return f"{obj.formation.title}"
    get_formation_name.short_description = 'formation'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
