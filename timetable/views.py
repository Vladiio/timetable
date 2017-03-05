# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import StreamingHttpResponse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Subject, Student, Mark


class IndexView(generic.ListView):
    template_name = 'timetable/index.html'
    context_object_name = 'subject_list'

    def get_queryset(self):
        return Subject.objects.all()


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user:

            auth.login(request, user)
            return redirect(reverse('timetable:index'))

    return render(request, 'timetable/login_error.html')


def get_mark(request):
    subject_id = request.GET.get('subject_id')
    user_id = request.user.id

    try:
        student = Student.objects.get(user_id=user_id)
        marks = Mark.objects.filter(student_id=student.id,
                                   subject_id=subject_id)

    except Student.DoesNotExist:
        result = u'Произошла ошибка, возможно вы не являетесь студентом'

    else:

        if not marks:
            result = u'У вас еще нет оценки по этому предмету'
        else:
            result = ''
            for mark in marks:
                result += str(mark) + '; '
            result = result[:-2]

    return StreamingHttpResponse(result)


def logout(request):
    auth.logout(request)
    return redirect(reverse('timetable:index'))
