from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('type','is_first_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'type'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
