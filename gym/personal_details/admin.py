from django.contrib import admin
from .models import PersonalDetails


# Register your models here.
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'contact', 'date_of_birth', 'gender', 'address_line', 'unit', 'postal_code')

    ordering = ('user',)

    filter_horizontal = ()
    list_filter = ()

    # Form fields when you edit existing accounts
    fieldsets = (
        (
            None,
            {'fields': ('user', 'contact', 'date_of_birth', 'gender', 'address_line', 'unit', 'postal_code',
                       )}),
    )

    # Form fields when you create new account

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'contact', 'date_of_birth', 'gender', 'address_line', 'unit', 'postal_code',
                       'emergency_contact', 'emergency_number'),
        }),
    )


admin.site.register(PersonalDetails, PersonalDetailsAdmin)
