from django.contrib import admin
from .models import Coins, CoinTag, CoinTagLink, ContactUs, CoinOffer


class CoinTagAdmin(admin.TabularInline):
    model = CoinTagLink
    fk_name = "coins"


class CoinsAdmin(admin.ModelAdmin):
    inlines = [CoinTagAdmin]
    model = Coins


admin.site.register(Coins, CoinsAdmin)
admin.site.register(CoinTag)
admin.site.register(ContactUs)
admin.site.register(CoinOffer)
