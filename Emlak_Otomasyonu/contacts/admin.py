from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Adı', 'Listeleme', 'E-posta', 'iletişim_tarihi')
    list_display_links = ('id', 'Adı')
    search_fields = ('Adı', 'E-posta', 'Listeleme')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)