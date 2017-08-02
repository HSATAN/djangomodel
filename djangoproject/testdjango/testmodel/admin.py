from django.contrib import admin
from  .models import  Test,Topic,Article
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','add_date')
    list_filter = ('add_date',)
    pass

'''
register有两个参数，第一个model，第一个参数可以是一个元组。第二个为修饰model的类
'''
admin.site.register(Topic,TopicAdmin)
admin.site.register((Test,Article))
