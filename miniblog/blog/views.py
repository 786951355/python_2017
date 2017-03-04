from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

from .models import Article, BlogComment, Tag
from .form import BlogCommentForm


def index(request):
    article_list = Article.objects.all()
    tag_list = Tag.objects.all()
    return render(request, 'blog/index.html', {'article_list': article_list, 'tag_list': tag_list})


def detail(request, article_id):
    comment_form = BlogCommentForm()
    article = Article.objects.get(id=article_id)
    comments = article.blogcomment_set.all().order_by('article__pub_date')
    tag_list = Tag.objects.all()
    return render(request, 'blog/detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form, 'tag_list': tag_list})


# 自定义评论
def comment(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.blogcomment_set.all()
    comment_form = BlogCommentForm()
    if request.method == 'POST':
        comment_post = BlogCommentForm(request.POST)
        if comment_post.is_valid():
            comment_info = comment_post.cleaned_data
            user_name = comment_info['user_name']
            user_email = comment_info['user_email']
            content = comment_info['content']
            comment = BlogComment.objects.create(user_name=user_name, user_email=user_email, content=content, article_id=article_id)
            comment.save()
            return HttpResponseRedirect('/'+ article_id)
        else:
            return HttpResponse('数据格式不合法')
    else:
        return render(request, 'blog/detail.html',{'article': article, 'comments': comments, 'comment_form': comment_form})


def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag_list = Tag.objects.all()
    article_list = tag.article_set.all()
    return render(request, 'blog/tagdetail.html', {'article_list': article_list, 'tag_list': tag_list})


def tag_detail(request, tag_id, article_id):
    return HttpResponseRedirect('/'+ article_id)


def search(request):
    article_list = []
    ks = request.GET.get('keywords')
    tag_list = Tag.objects.all()
    if ks:
        all_article = Article.objects.all()
        for article in all_article:
            if ks in article.title:
                article_list.append(article)
            elif ks in article.content:
                article_list.append(article)
        resultCount = len(article_list)
        return render(request, 'blog/searchresult.html', {'article_list': article_list,
                                                          'resultCount': resultCount,
                                                          'ks': ks,
                                                          'tag_list': tag_list})
    else:
        return render(request, 'blog/searchresult.html', {'article_list': article_list,
                                                          'ks': ks,
                                                          'tag_list': tag_list,
                                                          'error_message': 'error'})


def test(request):
    return render(request, 'test.html')