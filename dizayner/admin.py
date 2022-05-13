from django.contrib import admin

from .models.dizayner import Dizayner
from .models.portfolio import Portfolio, Portfolio_photo

from .models.proizvoditeli import Proizvoditeli


# Register your models here.

class Portfolio_foto_inlines(admin.StackedInline):
    model = Portfolio_photo

class Portfolio_foto_admins(admin.ModelAdmin):
    inlines = [Portfolio_foto_inlines]

admin.site.register(Dizayner)
admin.site.register(Portfolio, Portfolio_foto_admins)
admin.site.register(Proizvoditeli)