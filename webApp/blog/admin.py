from django.contrib import admin

# Register your models here.
from blog.models import Article


# 设置admin界面展示的样式
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ("title",'pub_date')

admin.site.register(Article, ArticleAdmin)