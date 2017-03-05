# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(max_length=40,
                                  verbose_name='Имя')
    surname = models.CharField(max_length=40,
                               verbose_name='Фамилия')
    user = models.ForeignKey(User,
                             verbose_name='Аккаунт')

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.surname)

    class Meta:
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'


class Student(models.Model):

    first_name = models.CharField(max_length=40,
                                  verbose_name=u'Имя')
    surname = models.CharField(max_length=40,
                               verbose_name=u'Фамилия')
    group = models.CharField(max_length=20,
                             verbose_name=u'Группа')

    user = models.ForeignKey(User,
                             related_name='student')

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.surname)

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'


class Subject(models.Model):
    title = models.CharField(max_length=40,
                             verbose_name=u'Название')
    time = models.TimeField(verbose_name=u'Начало')
    student = models.ManyToManyField(Student,
                                     related_name='subjects',
                                     verbose_name=u'Студенты')
    teacher = models.ForeignKey(Teacher,
                                related_name='subjects',
                                verbose_name=u'Учитель')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('time',)
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Mark(models.Model):
    VALUE_CHOICES = (
        (u'Нет оценки ', u'Нет оценки'),
        (u'Плохо ', '2'),
        (u'Удовлетворительно ', '3'),
        (u'Хорошо ', '4'),
        (u'Отлично ', '5'),
        )
    student = models.ForeignKey(Student, related_name='marks')
    subject = models.ForeignKey(Subject)
    value = models.CharField(max_length=20,
                             choices=VALUE_CHOICES,
                             default=u'Нет оценки')

    def __unicode__(self):
        return u'{}'.format(self.value)

    class Meta:
        verbose_name = u'Оценка'
        verbose_name_plural = u'Оценки'