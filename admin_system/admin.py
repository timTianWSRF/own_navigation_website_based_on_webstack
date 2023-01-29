from django.contrib import admin
from .models import Categories
from .models import Sites


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'order', 'title', 'icon', 'created_at', 'updated_at')
    list_display_links = ('id',)
    list_editable = ('parent_id', 'order', 'title', 'icon')
    list_filter = ('parent_id', )


class SitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'thumb', 'describe', 'url', 'created_at', 'updated_at')
    list_display_links = ('id',)
    list_editable = ('category', 'title', 'thumb', 'describe', 'url',)
    list_filter = ('category', )


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sites, SitesAdmin)
