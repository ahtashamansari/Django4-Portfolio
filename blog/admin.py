from django.contrib import admin

# Register your models here.

from .models import visitor , contact, Blog

admin.site.register(visitor)
admin.site.register(contact)
admin.site.register(Blog)