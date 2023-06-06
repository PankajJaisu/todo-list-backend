from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'tags')
        }),
        ('Date and Status', {
            'fields': ('created_at', 'due_date', 'status')
        }),
    )
    exclude = ('created_at','due_date',)
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    include = ('title','description','status','tags')
    list_display = ('name',)
    search_fields = ('name',)
