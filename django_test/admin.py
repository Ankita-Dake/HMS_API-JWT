from django.contrib import admin
from .models import PatientRecord, Department

admin.site.register(PatientRecord)
admin.site.register(Department)