from django.db import models

# Create your models here.
# 테이블은 하나의 클래스로 정의한다
class Bookmark(models.Model):

    title = models.CharField(max_length = 200)
    url = models.URLField('url', unique = True)

    def __str__(self):              #제목을 나타내는 함수
        return "%s %s" %(self.title, self.url)