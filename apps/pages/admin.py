from django.contrib import admin

from pages.models import Page


class PageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at',
        'updated_at',
        'is_active'
    )

    list_filter = ('is_active',)

    search_fields = ('title', 'content')

    ordering = ['-created_at']


admin.site.register(Page, PageAdmin)
