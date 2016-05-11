from django.contrib import admin
from .models import Club 
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class ClubAdmin(admin.ModelAdmin): pass

admin.site.register(Club, ClubAdmin)

