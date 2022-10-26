from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) # 제목
    content = models.TextField() # 본문

    created_at = models.DateTimeField(auto_now_add=True) # 시간날짜
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}' # f"" 문자열로 만들어줌