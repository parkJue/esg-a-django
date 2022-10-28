from django.shortcuts import redirect, render
from diary.models import Diary
from diary.forms import DiaryForm

# Create your views here.
def index(request):
    # 전체 포스팅을 가져올 준비
    # 이 시점(현재 6번째 줄)에서는 아직 가져오지는 않음
    diary_qs = Diary.objects.all().order_by("-pk")
    # render함수 : 일종의 장고 틀
    return render(request, "diary/index.html", {
        'diary_list' : diary_qs, # render함수의 세번째 인자
    })

def detail(request, pk):
    diary = Diary.objects.get(pk=pk)
    return render(request, 'diary/detail.html',{
        'diary': diary,
    })

def new(request):
    if request.method == "GET":
        form = DiaryForm()
    else:
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save()
            return redirect(diary)
    return render(request, 'diary/diary_form.html',{
        "form":form,
    })
# 수정
def new_edit(request, pk):
    memory = Diary.objects.get(pk=pk)
    if request.method == "GET":
        form = DiaryForm(instance=memory)
    else:
        form = DiaryForm(request.POST, instance=memory)
        if form.is_valid():
            diary = form.save()
            return redirect(diary)
    return render(request, 'diary/diary_form.html', {
        "form": form,
    })

def delete(request, pk):
    memory = Diary.objects.get(pk=pk)
    # TODO : delete memory
    if request.method == "POST":
        memory.delete()
        return redirect('/diary/')
    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })