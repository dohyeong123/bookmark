from django.contrib import admin
from django.urls import path
from bookmarkapp.views import bookmark_list, bookmark_detail
import bookmarkapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', bookmarkapp.views.bookmark_list, name = 'index'),
    path('bookmark/<int:bookmark_pk>/', bookmarkapp.views.bookmark_detail, name = 'detail'),
]
