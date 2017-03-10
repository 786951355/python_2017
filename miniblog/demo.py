import random

from learndjango.wsgi import *
from blog.models import Article,Author,Tag

author_name_list = ['lucy', 'google', 'ibm', 'redhat']
article_title_list = ['ansible 最佳实践', 'kvm 虚拟化', 'docker 从入门到放弃', 'mysql 从删库到跑路']


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

        for i in range(42, 52):
            title = '{}_{}'.format(article_title, i)
            article, created = Article.objects.get_or_create(
                title = title, defaults={
                    'author': random_author,
                    'content': '''{} Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

Ansible’s main goals are simplicity and ease-of-use. It also has a strong focus on security and reliability, featuring a minimum of moving parts, usage of OpenSSH for transport (with an accelerated socket mode and pull modes as alternatives), and a language that is designed around auditability by humans–even those not familiar with the program.

We believe simplicity is relevant to all sizes of environments, so we design for busy users of all types: developers, sysadmins, release engineers, IT managers, and everyone in between. Ansible is appropriate for managing all environments, from small setups with a handful of instances to enterprise environments with many thousands of instances.

Ansible manages machines in an agent-less manner. There is never a question of how to upgrade remote daemons or the problem of not being able to manage systems because daemons are uninstalled. Because OpenSSH is one of the most peer-reviewed open source components, security exposure is greatly reduced. Ansible is decentralized–it relies on your existing OS credentials to control access to remote machines. If needed, Ansible can easily connect with Kerberos, LDAP, and other centralized authentication management systems.

This documentation covers the current released version of Ansible (2.2) and also some development version features (2.3). For recent features, we note in each section the version of Ansible where the feature was added.

Ansible, Inc. releases a new major release of Ansible approximately every two months. The core application evolves somewhat conservatively, valuing simplicity in language design and setup. However, the community around new modules and plugins being developed and contributed moves very quickly, typically adding 20 or so new modules in each release.'''.format(title),
                    'score': random.randrange(70, 101)
                }
            )
            article.tags.add(tag)

if __name__ == '__main__':
    create_author()
    create_article_and_tags()
    print('done')


# SELECT "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" = 34