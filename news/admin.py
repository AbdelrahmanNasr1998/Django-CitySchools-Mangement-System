from django.contrib import admin
from .models import Post, Comment

class postData(admin.ModelAdmin):
    list_display = ('title','post_date')

class commentData(admin.ModelAdmin):
    list_display = ('full_name','comment_date','body')


admin.site.register(Post,postData)
admin.site.register(Comment,commentData)

