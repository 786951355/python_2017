import random

from learndjango.wsgi import *
from blog.models import Article,Author,Tag

author_name_list = ['page', 'loveroot', 'hack', 'test', 'mac']
article_title_list = ['django 教程', 'Linux 系统', '系统 架构', '开源 前端', 'python 运维开发']


def create_author():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        author.qq = ''.join(str(random.choice(range(10))) for _ in range(9))
        author.addr = 'addr_{}'.format(random.randrange(1,3))
        author.email = '{}@gmail.com'.format(author.addr)
        author.save()


def create_article_and_tags():
    for article_title in article_title_list:
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '{}_{}'.format(article_title, i)
            article, created = Article.objects.get_or_create(
                title = title, defaults={
                    'author': random_author,
                    'content': '{} 我不想成为一个庸俗的人。十年百年后，当我们死去，质疑我们的人同样死去，后人看到的是裹足不前、原地打转的你，还是一直奔跑、走到远方的我？'.format(title),
                    'score': random.randrange(70, 101)
                }
            )
            article.tags.add(tag)

if __name__ == '__main__':

    create_author()
    create_article_and_tags()
    print('done')


# SELECT "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" = 34