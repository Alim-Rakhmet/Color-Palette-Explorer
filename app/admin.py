from django.contrib import admin
from app import models

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')
    list_display_links = ('id', 'color')
    search_fields = ('id', 'color')

class PalitraAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')

admin.site.register(models.Color, ColorAdmin)
admin.site.register(models.Palitra, PalitraAdmin)