from django.contrib import admin

from . models import CarList

class CarListAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "model", "engine", "color", "price", "ratings", "carmanager_id", "is_published")
    list_display_links = ("id", "vendor", "model")
    list_editable = ("is_published",)
    search_fields = ("vendor", "price", "engine", "model", "ratings")
    list_per_page = 25
    list_filter = ("carmanager_id",)

admin.site.register(CarList, CarListAdmin)
