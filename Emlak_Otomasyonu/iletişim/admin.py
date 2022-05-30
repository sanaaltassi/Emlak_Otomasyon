from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'listeleme', 'eail', 'iletişim_tarihi')
    list_display_links = ('id', 'isim')
    search_fields = ('isim', 'mail', 'listeleme')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
