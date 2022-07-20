from email import contentmanager
from unicodedata import category
from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    kind = models.CharField(max_length=50, verbose_name="종류")
    content = models.TextField(verbose_name="개발툴 설명")

class Idea(models.Model):
    title = models.CharField(max_length=50, verbose_name="아이디어명")
    image = models.ImageField(blank = True, upload_to='', verbose_name="Image")
    content = models.TextField(verbose_name="아이디어 설명")
    interest = models.IntegerField(default = 0, verbose_name="아이디어 관심도")
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name="tool_name")
