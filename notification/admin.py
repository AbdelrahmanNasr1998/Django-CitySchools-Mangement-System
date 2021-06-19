from django.contrib import admin
from .models import Notification_A0, Notification_A1, Notification_A2, Notification_B1, Notification_B2, \
    Notification_B3, Notification_B4, Notification_B5, Notification_B6, Notification_C1, Notification_C2, \
    Notification_C3, Notification_D1, Notification_D2, Notification_D3, Comment_Notification_A0, \
    Comment_Notification_A1, Comment_Notification_A2, Comment_Notification_B1, Comment_Notification_B2, \
    Comment_Notification_B3, Comment_Notification_B4, Comment_Notification_B5, Comment_Notification_B6, \
    Comment_Notification_C1, Comment_Notification_C2, Comment_Notification_C3, Comment_Notification_D1, \
    Comment_Notification_D2, Comment_Notification_D3


# Register your models here.

class postData(admin.ModelAdmin):
    list_display = ('title','full_name','job','post_date')

class commentData(admin.ModelAdmin):
    list_display = ('full_name','job','post','comment_date','body')

admin.site.register(Notification_A0, postData)
admin.site.register(Notification_A1, postData)
admin.site.register(Notification_A2, postData)

admin.site.register(Notification_B1, postData)
admin.site.register(Notification_B2, postData)
admin.site.register(Notification_B3, postData)
admin.site.register(Notification_B4, postData)
admin.site.register(Notification_B5, postData)
admin.site.register(Notification_B6, postData)

admin.site.register(Notification_C1, postData)
admin.site.register(Notification_C2, postData)
admin.site.register(Notification_C3, postData)

admin.site.register(Notification_D1, postData)
admin.site.register(Notification_D2, postData)
admin.site.register(Notification_D3, postData)

#-----------------------------------------------

admin.site.register(Comment_Notification_A0, commentData)
admin.site.register(Comment_Notification_A1, commentData)
admin.site.register(Comment_Notification_A2, commentData)

admin.site.register(Comment_Notification_B1, commentData)
admin.site.register(Comment_Notification_B2, commentData)
admin.site.register(Comment_Notification_B3, commentData)
admin.site.register(Comment_Notification_B4, commentData)
admin.site.register(Comment_Notification_B5, commentData)
admin.site.register(Comment_Notification_B6, commentData)

admin.site.register(Comment_Notification_C1, commentData)
admin.site.register(Comment_Notification_C2, commentData)
admin.site.register(Comment_Notification_C3, commentData)

admin.site.register(Comment_Notification_D1, commentData)
admin.site.register(Comment_Notification_D2, commentData)
admin.site.register(Comment_Notification_D3, commentData)


