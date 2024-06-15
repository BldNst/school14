from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Avg
from .models import News, MenuItem, Teacher

def base(request):
    return render(request, 'index.html')

def news(request):
    news = News.objects.all().order_by('-pub_date')
    return render(request, 'news.html', {'news': news})

def one_new(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    vars = dict(
        title=post.title,
        body=post.content,
        timestamp=post.pub_date,
    )
    return render(request,'one_new.html', vars)

def menu_items(request, url):
    menu_items = MenuItem.objects.filter(url=url)
    return render(request, 'bases.html', {'menu_items':menu_items})


def teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher': teacher})

