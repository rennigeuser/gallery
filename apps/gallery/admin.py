from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'likes', 'created_at', )
    search_fields = ('title', )
    sortable_by = ('likes', 'created_at', )
    fieldsets = (
        ('Main', {
            'fields': ('author', 'title', ),
        }),
        ('Icon', {
            'fields': ('icon', 'icon_alt', ),
        }),
        ('Optional', {
            'fields': ('likes', ),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    save_as = True



@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    ...