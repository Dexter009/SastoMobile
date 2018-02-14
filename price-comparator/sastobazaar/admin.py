from django.contrib import admin

# Register your models here.
from .models import DarazItem, NepBayItem, SdealItem

admin.site.register(DarazItem)
admin.site.register(NepBayItem)
admin.site.register(SdealItem)