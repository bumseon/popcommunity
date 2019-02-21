from django.contrib import admin
from cms.models import Book, Impression
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'modify_date', 'clicks', 'up', 'content')
    list_display_links = ('id', 'name', ) # 속성 상세보기 링크 거는 기능

class ImpresstionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'replyname', 'replymodify_date')
    list_display_links = ('id', 'comment', )
    raw_id_fields = ('book',)

admin.site.register(Book, BookAdmin)
admin.site.register(Impression, ImpresstionAdmin)
