from django.contrib import admin
from .models import Subject, Student, Teacher


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'teacher')
    list_filter = ('time',)
    search_fields = ('title',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'group' )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
