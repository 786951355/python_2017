from django.db import models
from django.core.urlresolvers import reverse
from DjangoUeditor.models import UEditorField

# Create your models here.


class Author(models.Model):
    name = models.CharField('姓名', max_length=100)
    qq = models.CharField('QQ', max_length=10)
    addr = models.TextField('地址', max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'


class Article(models.Model):
    title = models.CharField('标题', max_length=150)
    author = models.ForeignKey(Author)
    # content = models.TextField('正文') # 原生字段
    content = UEditorField('内容', height=300, width=1000,default='', blank=True,imagePath="uploads/images/", toolbars='besttome', filePath='uploads/files/')
    score = models.IntegerField('评分')
    pub_date = models.DateTimeField('发表时间',auto_now_add=True, editable=True)
    update_date = models.DateTimeField('更新时间', auto_now=True, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #reverse('app_namespace:url_name', args, kwargs)
        return reverse('detail', args=(self.pk,))
        # return reverse('article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', args=(self.pk,))

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=20)
    user_email = models.EmailField('评论者邮箱',max_length=100)
    content = models.TextField('评论内容')
    create_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

