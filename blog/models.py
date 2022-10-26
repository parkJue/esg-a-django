from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) # 제목
    content = models.TextField() # 본문

    created_at = models.DateTimeField() # 시간날짜

    def __str__(self):
        return self.title
