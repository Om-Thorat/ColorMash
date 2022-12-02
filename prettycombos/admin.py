from django.contrib import admin

# Register your models here.
from .models import colorcombos as ccs

admin.site.register(ccs)