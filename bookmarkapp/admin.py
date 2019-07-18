from django.contrib import admin
from .models import Bookmark
# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):  #어떤 모습으로 사이트에서 보여줄지를 정하는 클래스
    list_display = ('title', 'url')

admin.site.register(Bookmark, BookmarkAdmin)

