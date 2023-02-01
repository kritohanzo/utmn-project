from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'is_published', 'is_deleted')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('text', 'author', 'is_published', 'is_deleted')
    empty_value_display = '-пусто-'
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post', 'is_published', 'is_deleted')
    list_editable = ('text', 'author', 'is_published', 'is_deleted')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
