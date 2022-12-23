from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    ...