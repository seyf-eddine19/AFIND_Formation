from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Formation, Enrollment, FormationImage, ContactMessage, SiteContent, SiteSettings, SiteSettings
from django.urls import path
from .admin_actions import export_as_csv, import_from_csv


admin.site.site_header = 'AFIND Frormation'   # default: "Django Administration"
admin.site.index_title = 'Administration'   # default: "Site administration"
admin.site.site_title = 'Administration'               # default: "Django site admin"
Group._meta.verbose_name = 'Permissions Group'
Group._meta.verbose_name_plural = 'Permissions Groups'


class FormationImageInline(admin.TabularInline):
    model = FormationImage
    extra = 1


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'department', 'date', 'status')
    search_fields = ('title', 'department')
    list_filter = ('department', 'instructor')
    
    inlines = [FormationImageInline]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('get_formation_name', 'full_name', 'specialty', 'enrollment_date', 'source', 'status')
    search_fields = ('full_name', 'phone', 'formation__title', 'formation__session', 'specialty')
    list_filter = ('status', 'enrollment_date', 'specialty', 'formation__title', 'formation__session')
    list_editable = ('status',)
    actions = [export_as_csv]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ('source',)
        return readonly_fields
    
    def get_formation_name(self, obj):
        return f"{obj.formation.title}"
    get_formation_name.short_description = 'Formation'

    def import_csv(self, request):
        return import_from_csv(self, request)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import-csv/', self.import_csv),
        ]
        return new_urls + urls 
    

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'content')

    def has_add_permission(self, request):
        if SiteContent.objects.count() >= len(SiteContent.CONTENT_TYPE_CHOICES):
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'setting_value']

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_add_permission(self, request):
        if SiteContent.objects.count() >= len(SiteContent.CONTENT_TYPE_CHOICES):
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
