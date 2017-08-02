#coding=utf8

from django import forms
from  .models import Test
class NameForm(forms.ModelForm):
    class Meta:
        model=Test
        fields=['name','age']
        labels={'name':"请输入要存到数据库的姓名:",'age':'请输入年龄'}