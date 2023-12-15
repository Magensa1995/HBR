from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'bio']
# Register your models here.
admin.site.register(User, UserAdmin)