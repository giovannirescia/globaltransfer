from django.contrib import admin
from billingsystem.models import Taxi, Bill


class BillAdmin(admin.ModelAdmin):
    list_display = ['billed_date', 'total_cash','bill_id','taxi', 'user', 'paid',]
    list_filter = ['billed_date','user','taxi']
    search_fields = ['user__username','taxi__taxi_id']

admin.site.register(Bill, BillAdmin)
admin.site.register(Taxi)
