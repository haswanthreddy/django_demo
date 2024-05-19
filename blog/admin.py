from django.contrib import admin
from .models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'username', 'address']
    list_display = ['name', 'username']
    search_fields = ['name']

# can be used the above way with decorators or the below way, the one with decorators is more preffered 


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'author', 'description']
    search_fields = ['title']


admin.register(Post, PostAdmin)

