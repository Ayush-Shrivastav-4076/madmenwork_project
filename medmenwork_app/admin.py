from django.contrib import admin
from .models import Banner, Client, SliderImage
from .models import Contact
from .models import LeatherProduct

admin.site.register(Banner)
admin.site.register(Client)
admin.site.register(SliderImage)
admin.site.register(Contact)

class LeatherProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'description')
    list_filter = ('category',)
    search_fields = ('description',)

admin.site.register(LeatherProduct, LeatherProductAdmin)