from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, BlogComment, Tag, AccessIp
from .form import BlogCommentForm
import datetime


def index(request):
    article_list = Article.objects.all().order_by('-pub_date')
    tag_list = Tag.objects.all()
    return render(request, 'blog/index.html', {'article_list': article_list, 'tag_list': tag_list})


def detail(request, article_id):
    comment_form = BlogCommentForm()
    article = Article.objects.get(id=article_id)
    comments = article.blogcomment_set.all().order_by('article__pub_date')

    # 获取当前文章的上一页，下一页
    post = get_object_or_404(Article, id=article_id)
    article = Article.objects.get(id=article_id)
    page_list = list(Article.objects.all())
    if post == page_list[-1]:
        before_page = page_list[-2]
        after_page = None
    elif post == page_list[0]:
        before_page = None
        after_page = page_list[1]
    else:
        situ = page_list.index(post)
        before_page = page_list[situ - 1]
        after_page = page_list[situ + 1]

    # 判断当前ip是否访问过此文章，没访问过记录ip和访问时间，访问过如果时间超过1小时则阅读量加1，并更新访问时间
    tag_list = Tag.objects.all()
    tag = article.tags.all()[0].name
    client_ip = request.environ.get('REMOTE_ADDR')
    d = dict()
    ip_list = ((ip.ipaddr, ip.id) for ip in article.accessip.all())
    for k, v in ip_list:
        d[k] = v

    if client_ip in d:
        access_time = AccessIp.objects.get(id=d[client_ip]).access_time.replace(tzinfo=None)
        now = datetime.datetime.utcnow()
        delta_time = now - access_time
        if delta_time.total_seconds() > 3600:
            article.times += 1
            article.accessip.add(AccessIp.objects.update(ipaddr=client_ip, access_time=datetime.datetime.now()))
            article.save()
            return render(request, 'blog/detail.html', {'article': article, 'tag': tag, 'access_times': article.times,
                                                        'comments': comments, 'comment_form': comment_form, 'tag_list': tag_list,
                                                        'post': post, 'before_page': before_page,'after_page': after_page})

        return render(request, 'blog/detail.html', {'article': article, 'tag': tag, 'access_times': article.times,
                                                    'comments': comments, 'comment_form': comment_form, 'tag_list': tag_list,
                                                    'post': post, 'before_page': before_page, 'after_page': after_page})
    else:
        article.times += 1
        article.accessip.add(AccessIp.objects.create(ipaddr=client_ip, access_time=datetime.datetime.now()))
        article.save()
        return render(request, 'blog/detail.html', {'article': article, 'tag': tag, 'access_times': article.times,
                                                    'comments': comments, 'comment_form': comment_form, 'tag_list': tag_list,
                                                    'post': post, 'before_page': before_page, 'after_page': after_page})

# 自定义评论, 用了多说此处多余
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


def tag_cloud(request):
    tag_list = Tag.objects.all()
    return render(request, 'footer.html', {'tag_list': tag_list})


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