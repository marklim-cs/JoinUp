from django.contrib import admin
from users.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

admin.site.register(UserProfile, UserProfileAdmin)