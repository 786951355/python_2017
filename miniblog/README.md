# readme
# 默认密码： admin miniblog
# 普通用户       loveroot helloworld
```
后台使用了DjangoUeditor  由于原作者没有更新，所以fork了一份改了下原代码兼容python 3
安装 pip install git+https://github.com/786951355/DjangoUeditor
快速测试没有使用Mysql等数据库，直接使用了sqlite3
使用方法请看readme文档

```
# 首页
![image](https://github.com/786951355/python_2017/raw/master/index.jpg)
# 后台
![image](https://github.com/786951355/python_2017/raw/master/admin.jpg)
# 文章列表
![image](https://github.com/786951355/python_2017/raw/master/article_list.jpg)
# 文章编辑页
![image](https://github.com/786951355/python_2017/raw/master/article_edit.jpg)
# 搜索效果
![image](https://github.com/786951355/python_2017/raw/master/search.jpg)
# 文件详情页1
![image](https://github.com/786951355/python_2017/raw/master/article_detail.jpg)
# 文章详情2
![image](https://github.com/786951355/python_2017/raw/master/article_detail2.jpg)

```
uwsgi + nginx
========================
安装uwsgi
pip install uwsgi

配置uwsgi配置文件，方便supervisor命令管理

# myweb_uwsgi.ini file
[uwsgi]

# Django-related settings

socket = 127.0.0.1:8000

# the base directory (full path)
chdir           = /opt/miniblog/learndjango

# Django s wsgi file
module          = learndjango.wsgi

# process-related settings
# master
master          = true

# maximum number of worker processes
processes       = 4

# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true

尝试使用uwsgi启动看看能不能成功
uwsgi --ini miniblog_uwsgi.ini


------------------------------------------
使用supervisor 管理uwsgi
yum install supervisor
service supervisord start
cat /etc/supervisord.conf
最后加上 

[program:miniblog]
user=root
command=/root/.pyenv/shims/uwsgi --ini /opt/miniblog/learndjango/miniblog_uwsgi.ini
directory=/opt/miniblog/learndjango
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true


安装nginx

修改配置文件

server
    {
        listen 8558 default_server;
        #listen [::]:80 default_server ipv6only=on;

        #error_page   404   /404.html;


    location  / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        uwsgi_read_timeout 8;
    }


    location /static/ {
        root /opt/miniblog/learndjango;
    }
    
    location /media/ {
        root /opt/miniblog/learndjango;
    }


        access_log  /home/wwwlogs/access.log  access;
    }


```
