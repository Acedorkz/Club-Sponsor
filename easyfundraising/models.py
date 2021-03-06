# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField('用户名',max_length=30)
    password = models.CharField('密码',max_length=30)
    email = models.EmailField('邮箱')
    def __unicode__(self):
        return self.username
   
class Item(models.Model):
    author = models.ForeignKey(User,related_name='items',default=0)
    title = models.CharField(max_length=30)
    contents =RichTextUploadingField("contents")
    pubtime = models.DateTimeField(auto_now=True)
    contacts = models.CharField(max_length=50)
    def __unicode__(self):
        return self.title
class UserDetail(models.Model):
    user = models.OneToOneField(User,related_name='infos',default=0)
    school = models.CharField("学校",max_length=50)
    social_name = models.CharField("社团名",max_length=50)
    phone_num = models.CharField(max_length=11,verbose_name='电话号码')
    def __unicode__(self):
        return self.social_name

    
    
