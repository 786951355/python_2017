from django.conf.urls import url

from . import views

# url命名空间在进行url反解析的时候可以区别，以免重复
app_name = 'blog'

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'(?P<slug>[^/]+)', views.detail, name='detail'),
#     # url(r'add/', views.add, name='add'),
#     # url(r'delete/', views.delete, name='delete'),
#     # url(r'update/', views.update, name='update'),
# ]