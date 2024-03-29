from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # section1
        (_('Personal Info'), {'fields': ('name',)}),  # section2
        (_('Permissions'), {'fields': ('is_active',
                                       'is_staff', 'is_superuser')}),  # section3
        (_('Important Dates'), {'fields': ('last_login',)})  # section4
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
