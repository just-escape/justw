from django.contrib import admin

from salesquote.models import SalesQuote, SalesQuoteModelForm


class SalesQuoteAdmin(admin.ModelAdmin):
    form = SalesQuoteModelForm
    ordering = ('-submitted',)
    list_display = (
        'submitted',
        'contact_name',
        'company_name',
        'contact_email',
        'contact_number',
        'group_size',
        'desired_date',
        'discount_code',
        'comment',
    )
    search_fields = (
        'contact_name',
        'company_name',
        'contact_email',
        'contact_number',
        'comment',
    )


admin.site.register(SalesQuote, SalesQuoteAdmin)
