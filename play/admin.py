from django.contrib import admin
from .models import Play

# Register your models here.
@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','time','timestamp','owner','num_of_participants']
    ordering = ['-num_of_participants']
