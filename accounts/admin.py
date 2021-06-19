from django.contrib import admin
from .models import User, Specialist, Teacher, ProComment, A0, A1, A2, B1, B2, B3, B4, B5, B6, C1, C2, C3, \
    D1, D2, D3, Blogger, Application


class User_A(admin.ModelAdmin):
    list_display = ('full_name','is_Specialist','is_teacher','is_Blogger','is_responsible','is_student')



class staff(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'phone_number')


class Student_A(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'classroom', 'absent', 'late')

class pro_comment(admin.ModelAdmin):
    list_display = ('full_name', 'profile', 'comment_date', 'body')


class application(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'application_date')

admin.site.register(User,User_A)
admin.site.register(Blogger,staff)
admin.site.register(Specialist,staff)
admin.site.register(Teacher,staff)

admin.site.register(A0,Student_A)
admin.site.register(A1,Student_A)
admin.site.register(A2,Student_A)
admin.site.register(B1,Student_A)
admin.site.register(B2,Student_A)
admin.site.register(B3,Student_A)
admin.site.register(B4,Student_A)
admin.site.register(B5,Student_A)
admin.site.register(B6,Student_A)
admin.site.register(C1,Student_A)
admin.site.register(C2,Student_A)
admin.site.register(C3,Student_A)
admin.site.register(D1,Student_A)
admin.site.register(D2,Student_A)
admin.site.register(D3,Student_A)

admin.site.register(ProComment,pro_comment)

admin.site.register(Application,application)