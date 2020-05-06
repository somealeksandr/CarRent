from django.contrib import admin

from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    display = ('id', 'name', 'car', 'phone', 'contact-date')
    display_links = ('id', 'name', 'email', 'car')
    search_filter = ('name', 'email', 'car')
    pagination = 25
    
admin.site.register(Contacts, ContactAdmin)
