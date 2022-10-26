from django.shortcuts import render
from blog.models import Post

def index(request):
    # 전체 포스팅을 가져올 준비
    # 이 시점에서는 아직 가져오지는 않음
    post_qs = Post.objects.all().order_by("-pk")
    # render함수 : 일종의 장고 틀
    return render(request, "blog/index.html", {
        # post_qs값을 post_list라는 이름으로 참조하라
        'post_list' : post_qs, # render함수의 세번째 인자
    })
