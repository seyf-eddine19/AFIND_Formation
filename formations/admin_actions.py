# admin_actions.py
from django.http import HttpResponse
from datetime import datetime
import csv

def export_as_csv(modeladmin, request, queryset):
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"export_{current_date}.csv"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    writer = csv.writer(response)
    fields = [field.name for field in queryset.model._meta.fields]
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response

export_as_csv.short_description = "Export selected objects as CSV"


