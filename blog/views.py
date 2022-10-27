from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from blog.forms import PostForm
from blog.rest_forms import RestForm
from blog.models import Post, Restaurant
from django.views.generic import CreateView
def index(request):
    # 전체 포스팅을 가져올 준비
    # 이 시점(현재 6번째 줄)에서는 아직 가져오지는 않음
    post_qs = Post.objects.all().order_by("-pk")
    # render함수 : 일종의 장고 틀
    return render(request, "blog/index.html", {
        # post_qs값을 post_list라는 이름으로 참조하라
        'post_list' : post_qs, # render함수의 세번째 인자
    })

def single_post_page(request, pk):
    post = Post.objects.get(pk = pk)

    return render(request, 'blog/single_post_page.html', {
        'post':post,
    })

# post_new = CreateView.as_view(
#     form_class = PostForm,
#     model=Post,
#     success_url = "/blog/",
# )

def post_new(request):
    # print("request.method =", request.method)
    # print("request.POST=", request.POST)
    if request.method == "GET":
        form =  PostForm()
    else: # POST라면
        form = PostForm(request.POST)
        if form.is_valid(): # 유효성 검사가 모두 통과해야 true 반환
            # 유효성 검사가 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/") 
            # return redirect(f"/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
    return render(request, "blog/post_form.html", {
        "form" : form,
    })

def restaurants_list(request):
    post_qs = Restaurant.objects.all().order_by("-pk")
    return render(request, "blog/restaurants_list.html", {
        'post_list' : post_qs, # render함수의 세번째 인자
    })

def rest_post_page(request, pk):
    post = Restaurant.objects.get(pk = pk)

    return render(request, 'blog/rest_post_page.html', {
        'post':post,
    })

def rest_new(request):
    if request.method == "GET":
        form =  RestForm()
    else: # POST라면
        form = RestForm(request.POST)
        if form.is_valid(): # 유효성 검사가 모두 통과해야 true 반환
            # 유효성 검사가 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/") 
            # return redirect(f"/blog/restaurants/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
    return render(request, "blog/rest_form.html", {
        "form" : form,
    })
