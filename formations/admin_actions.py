
import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Enrollment, Formation 
from .forms import CSVImportForm
from datetime import datetime

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


def import_from_csv(modeladmin, request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]

        # Check if the file is a CSV file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        # Assume the first row is the header
        reader = csv.DictReader(lines)

        for r, row in enumerate(reader):
            # You need to parse your CSV rows according to your model fields
            formation_title = row.get('formation_title')
            formation_session = row.get('formation_session')
            # Get or create the formation based on title and session
            formation, created = Formation.objects.get_or_create(
                title=formation_title, 
                session=formation_session
            )
            try:
                enrollment = Enrollment(
                    formation=formation,
                    full_name=row.get('full_name'),
                    email=row.get('email'),
                    phone=row.get('phone'),
                    region=row.get('region'),
                    specialty=row.get('specialty'),
                    source=row.get('source'),
                    status=row.get('status'),
                    enrollment_date=row.get('enrollment_date'),
                )
                enrollment.save()
            except Exception as e:
                messages.error(request, f'Can not import row {r} \n{e}')

        return HttpResponseRedirect(request.get_full_path())

    form = CSVImportForm()
    return render(
        request, "admin/csv_form.html", {"form": form}
    )

import_from_csv.short_description = "Import from CSV"
