from django.shortcuts import render, get_object_or_404
from .models import Bookmark
# Create your views here.

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    print(bookmarks)
    return render(request, 'bookmark/bookmark_list.html', {'bookmark_list': bookmarks})

def bookmark_detail(request, bookmark_pk):      #pk를 설정해줄 때 detail함수에 인자로 pk가 아닌 bookmark_pk로 설정해주어야한다
    bookmark = get_object_or_404(Bookmark, pk=bookmark_pk)
    context = {'bookmark': bookmark}
    return render(request, 'bookmark/bookmark_detail.html', context)