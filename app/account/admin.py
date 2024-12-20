""" Django admin customizing. """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """ Define the admin pages for users. """
    ordering = ['id']
    list_display = ['mobile_number', 'name', 'surname']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name',
         'surname', 'mobile_number', 'birth_date', 'gender')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login',]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'surname',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Wishlist)
