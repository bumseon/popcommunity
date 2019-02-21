from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField('제목', max_length=100)
    publisher = models.CharField('작성자', max_length=100, blank=True)
    
    modify_date = models.DateTimeField('등록일', auto_now_add=True)
    clicks = models.IntegerField('조회수', blank=True, default=0)
    up = models.IntegerField('추천', blank=True, default=0)
    content = models.TextField('내용', blank=True)
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.name

    

        # 번호 제목 글쓴이 등록일 조회수 추천
class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name='도서', related_name='impressions', on_delete=models.CASCADE)
    replyname = models.CharField('작성자', max_length=100, blank=True)
    comment = models.TextField('댓글', blank=True)
    
    replymodify_date = models.DateTimeField('등록일', auto_now_add=True)
    def __str__(self):
        return self.comment

