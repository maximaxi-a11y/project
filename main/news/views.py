from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.shortcuts import render, get_object_or_404
from .models import News


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


def news_list(request):
    news = News.objects.all()   
    return render(request, 'news/news_list.html', {'news': news})




def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user  
            news.save()
            return redirect('news_list')  
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})