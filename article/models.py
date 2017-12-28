from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length=100) #博客标题
    tag = models.CharField(max_length=50,blank=True) #博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = models.TextField(blank=True,null=True) #博客正文

    # 通过逆向解析 得到 url
    def get_absolute_url(self):
        path = reverse('content', kwargs={'id': self.id})
        print(path)
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time'] # 按照时间降序排列

