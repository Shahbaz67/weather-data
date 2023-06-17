from django.contrib import admin
from weather_info.models import Summary

class SummaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Summary, SummaryAdmin)
