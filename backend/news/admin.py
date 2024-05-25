from django.contrib import admin
from .models import New, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')
    search_fields = ('title', 'text')
    list_filter = ('created_at', 'tags')

admin.site.register(New, NewsAdmin)
admin.site.register(Tag)