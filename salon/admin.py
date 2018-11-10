from django.contrib import admin
from .models import *
from .forms import *


class PriceItemInline(admin.TabularInline):
    model = PriceItem
    form = PriceItemForm
    fk_name = 'for_inline'


class PriceItemModelAdmin(admin.ModelAdmin):
    model = PriceItem
    form = PriceItemForm
    inlines = (PriceItemInline,)


admin.site.register(PriceItem, PriceItemModelAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ImageCard)
admin.site.register(InstagramLink)
admin.site.register(Contact)
