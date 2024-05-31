from django.contrib import admin
from .models import Banner, Client, SliderImage,LeatherProduct,Contact, Settings,TeamMember,Activity


admin.site.register(Banner)
admin.site.register(Client)
admin.site.register(SliderImage)
admin.site.register(Contact)
admin.site.register(Settings)
admin.site.register(TeamMember)
admin.site.register(Activity)



class LeatherProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'description')
    list_filter = ('category',)
    search_fields = ('description',)

admin.site.register(LeatherProduct, LeatherProductAdmin)

