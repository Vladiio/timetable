from django.contrib import admin
from .models import Mark, Subject, Student, Teacher


class MarkStacked(admin.StackedInline):
    model = Mark


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'teacher')
    list_filter = ('time',)
    search_fields = ('title',)
    inlines = [MarkStacked]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'group')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
