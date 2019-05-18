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
        'prestation_type',
        'option_cocktail_with_alcool',
        'option_cocktail_without_alcool',
        'option_privatisation',
        'desired_date',
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
