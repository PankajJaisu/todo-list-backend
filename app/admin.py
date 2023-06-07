from django.contrib import admin
from .models import *


#Added the required filter based on the Assignment Given

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Task Information', {

            'fields': ('title', 'description', 'tags')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )
    
    list_display = ('title', 'status', 'due_date','created_at',) 
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
