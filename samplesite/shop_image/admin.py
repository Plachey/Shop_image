from django.contrib import admin
from .models import Image, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ImageAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
