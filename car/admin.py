from django.contrib import admin
from .models import Car
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('url',)}
    list_display = ['url','play_object']