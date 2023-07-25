from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Block)

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author', 'created', 'status']
    list_filter = ['author', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['status', 'published']