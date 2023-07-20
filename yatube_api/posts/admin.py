from django.contrib import admin

from .models import Comment, Group, Post

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
