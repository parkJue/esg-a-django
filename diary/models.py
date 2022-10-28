from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 향후에는 장고 URL Reverse 기능 사용해보기
        return f"/diary/{ self.pk }/"
    
    def __str__(self):
        return f'[{self.pk}] {self.title}' # f"" 문자열로 만들어줌