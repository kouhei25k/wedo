from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,UserRelationship



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('joining_room',)}),)
    list_display = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserRelationship)