from django.contrib import admin

from . models import CarManager

class CarManagersAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    list_display_links = ("name", "phone", "email")
    search_fields = ("name", "email")
    list_per_page = 25
    list_filter = ("name",)

admin.site.register(CarManager, CarManagersAdmin)
