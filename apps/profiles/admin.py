from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.http import HttpResponse

from .models import User
import csv


class UserAdmin(BaseUserAdmin):
    inlines = [

    ]
    fieldsets = (
        (None,
         {'fields': ('username', 'phone_number', 'email', 'password', 'twitter', 'instagram', 'facebook')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # readonly_fields = ('image_tag',)

    list_display = ("username", "first_name", "last_name", "phone_number", "email", "twitter", "instagram", "facebook")
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        # writer.writerow(field_names)
        writer.writerow(["Date Joined", "First Name", "Last Name", "Phone Number", "Email", "Twitter", "Instagram", "Facebook"])
        for obj in queryset:
            # row = writer.writerow([getattr(obj, field) for field in field_names])
            line = []
            for field in field_names:
                if field == "date_joined" or field == "first_name" or field == "last_name" or \
                                field == "phone_number" or field == "email" or field == "twitter" or \
                                field == "instagram" or field == "facebook":
                    line.append(getattr(obj, field))

            row = writer.writerow(line)
        return response

    export_as_csv.short_description = "Export selected users to CSV"


admin.site.register(User, UserAdmin)
