# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models




# Create your models here.
class User(models.Model):
    username = models.CharField('用户名',max_length=30)
    password = models.CharField('密码',max_length=30)
    email = models.EmailField('邮箱',unique=True)
    def __unicode__(self):
        return self.username
   
class Item(models.Model):
    choice=(('club','社团'),
                    ('market','商家'),)
    kind = models.CharField(max_length=4,choices=choice,default='club',)
    author = models.CharField('作者',max_length=20)
    title = models.CharField('题目',max_length=30)
    contents =RichTextUploadingField("内容")
    pubtime = models.DateTimeField(auto_now=True)
    contacts = models.CharField('联系方式',max_length=50)
    class Meta:
        ordering=['pubtime']
        
        
    
    def __unicode__(self):
        return self.title
class UserDetail(models.Model):
    user = models.OneToOneField(User,related_name='infos',default=0)
    school = models.CharField("学校",max_length=50)
    social_name = models.CharField("社团名",max_length=50)
    phone_num = models.CharField(max_length=11,verbose_name='电话号码')
    def __unicode__(self):
        return self.social_name

    
    
