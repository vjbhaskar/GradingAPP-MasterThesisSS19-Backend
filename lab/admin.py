from django.contrib import admin
from .models import Lab, LabIp, Time_Slot

# Register your models here.
admin.site.register(Lab)
admin.site.register(LabIp)
admin.site.register(Time_Slot)