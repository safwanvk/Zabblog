from django.contrib import admin

# Register your models here.
from .models import Blog, Contact

admin.site.register(Blog)
admin.site.register(Contact)
