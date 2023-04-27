from django.contrib import admin
from .models import Email

# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    search_fields = ['email']


admin.site.register(Email, EmailAdmin)