from django.contrib import admin
from drvb.models import Driver, Referral, Company

class DriverAdmin(admin.ModelAdmin):
    pass

admin.site.register(Driver, DriverAdmin)

class ReferralAdmin(admin.ModelAdmin):
    pass

admin.site.register(Referral, ReferralAdmin)

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)