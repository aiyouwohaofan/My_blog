from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from datetime import datetime
from django.core.paginator import Paginator


def article_list(request):
    articles = Article.objects.all()

    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles}
    return render(request, 'blog/article_list.html', context=context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.commentator = request.user
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', id)
        else:
            return HttpResponse('请重新填写')

    if request.user != article.author:
        article.article_views += 1
        article.save(update_fields=['article_views'])
    context = {'article': article, 'comments': comments}
    return render(request, 'blog/article_detail.html', context=context)


def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('article_list')
        else:
            return HttpResponse('请重新填写')
    else:
        article_form = ArticleForm()
        context = {'article_form': article_form}
        return render(request, 'blog/article_create.html', context=context)


def article_edit(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.modified_date = datetime.now()
            article.save()
            return redirect('article_detail', id)
        else:
            HttpResponse('表单内容有误，请重新填写')
    else:
        context = {'article': article}
        return render(request, 'blog/article_edit.html', context=context)


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('article_list')

