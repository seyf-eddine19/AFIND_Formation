from django.contrib import admin
from .models import Formation, Enrollment, FormationImage
from .admin_actions import export_as_csv

class FormationImageInline(admin.TabularInline):
    model = FormationImage
    extra = 1  # Number of empty form rows to show

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'department', 'enrollment_deadline', 'status')
    search_fields = ('title', 'department')
    list_filter = ('department', 'instructor')
    
    inlines = [FormationImageInline]

    # list_display = ('title', 'get_instructor_name', 'department')
    # search_fields = ('title', 'department')
    # list_filter = ('department', 'instructor__full_name')
    
    # inlines = [FormationImageInline]


    # def get_instructor_name(self, obj):
    #     return f"{obj.instructor.full_name}"
    # get_instructor_name.short_description = 'Instructor'
# admin.site.register(Formation, FormationAdmin)
    
# @admin.register(Instructor)
# class InstructorAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'phone', 'specialization')
#     search_fields = ('full_name', 'phone', 'specialization')
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'get_formation_name', 'department', 'academic_level', 'enrollment_date', 'status')
    search_fields = ('full_name', 'phone', 'specialization')

    list_filter = ('department', 'formation__title')
    actions = [export_as_csv]
    def get_formation_name(self, obj):
        return f"{obj.formation.title}"
    get_formation_name.short_description = 'formation'
