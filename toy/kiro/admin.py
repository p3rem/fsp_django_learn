from django.contrib import admin
from .models import user,student

# Register your models here.
admin.site.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'age', 'email', 'dept')
    search_fields = ('name', 'email', 'dept')
    list_filter = ('dept', 'age')
    
admin.site.register(student)
class StudentAdmin(admin.ModelAdmin):
   
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

