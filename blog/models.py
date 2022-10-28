from django.db import models
from django.core.validators import MaxValueValidator

class Restaurant(models.Model):
    """맛집"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5), # 숫자 5를 넘을 수 없다.
        ]
    )
    def __str__(self):
        return f'[{self.pk}] {self.name}' # f"" 문자열로 만들어줌
    
    def get_absolute_url(self):
        # TODO : 향후에는 장고 URL Reverse 기능 사용해보기
        return f"/blog/restaurants/{ self.pk }/"

class Post(models.Model):
    title = models.CharField(max_length=30) # 제목
    content = models.TextField() # 본문

    created_at = models.DateTimeField(auto_now_add=True) # 시간날짜
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 향후에는 장고 URL Reverse 기능 사용해보기
        return f"/blog/{ self.pk }/"
    
    def __str__(self):
        return f'[{self.pk}] {self.title}' # f"" 문자열로 만들어줌

    class Meta:
        # 쿼리셋에서 order_by를 지정하지 않았을 때 사용
        ordering=['-id']