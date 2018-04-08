from django.contrib import admin
from .models import Assignment

# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,{'fields':['serviceprovider','institution','status']}),
        ('Assignment Details',{'fields':['serviceprovider','institution','status']}),   
    ]
admin.site.register(Assignment,AssignmentAdmin)
