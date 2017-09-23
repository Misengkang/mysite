from django.contrib import admin
from .models import Post, Category, Tag


admin.site.site_header = "Kangkang Blog"


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    list_filter = ['create_time']
    search_fields = ['body']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


