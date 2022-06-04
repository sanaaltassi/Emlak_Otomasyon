from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Başlık', 'yayınlandı', 'fiyat', 'liste_tarihi', 'emlakçı')
    list_display_links = ('id', 'Başlık')
    list_filter = ('emlakçı',)
    list_editable = ('yayınlandı',)
    search_fields = ('Başlık', 'tanım', 'adres', 'Kent', 'konum', 'posta kodu', 'fiyat')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
