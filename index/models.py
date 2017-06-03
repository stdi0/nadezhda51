# coding: utf8

from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    SECTION_CHOICES = (
        (u'Docs', u'Документы'),
        (u'Events', u'События'),
        (u'Announce', u'Анонсы'),
        (u'Links', u'Ссылки'),
    )
    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField(u'Заголовок', max_length=200)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(u'Дата создания', default=timezone.now)
    section = models.CharField(u'Раздел', max_length=10, default='Docs', choices=SECTION_CHOICES)

    class Meta:
        verbose_name = u'Новости'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Activities(models.Model):
    SECTION_CHOICES = (
        (u'Announce', u'Анонсы'),
        (u'Past', u'Прошедшее'),
    )
    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField(u'Заголовок', max_length=200)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(u'Дата создания', default=timezone.now)
    section = models.CharField(u'Раздел', max_length=10, default='Announce', choices=SECTION_CHOICES)
    
    class Meta:
        verbose_name = u'Мероприятия'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Projects(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField(u'Заголовок', max_length=200)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(u'Дата создания', default=timezone.now)
    
    class Meta:
        verbose_name = u'Проекты'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
