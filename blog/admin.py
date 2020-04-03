from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Clinicalmanager)
admin.site.register(Regional)
admin.site.register(Requestforregionalmanager)
admin.site.register(SourcingTeam)
admin.site.register(Document)
# admin.site.register(Areamanager)