from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def index(request):
    # 모든 article 보여주는 페이지
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(request.POST)
    context = {'form':form}
    return render(request, 'articles/create.html', context)

    
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)