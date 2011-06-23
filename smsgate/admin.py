from smsgate.models import *
from django.contrib import admin


class IPRangeInline(admin.TabularInline):
    model = IPRange


class PartnerAdmin(admin.ModelAdmin):
    inlines = [
        IPRangeInline,
    ]


admin.site.register(Partner, PartnerAdmin)