from django.contrib import admin

from .models import Param, ParamName, Detail, DetailType, Car, Brand, CarPrice


class CarPriceAdmin(admin.ModelAdmin):
    readonly_fields = ("cost_price", "price")


admin.site.register(Param)
admin.site.register(Detail)
admin.site.register(DetailType)
admin.site.register(ParamName)
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(CarPrice, CarPriceAdmin)
