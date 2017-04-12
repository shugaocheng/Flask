在现有项目上进行了更改：
1.增加管理员后台权限，可以对文章进行增删查改、用户权限升降、栏目编辑等功能
2.增加消息推送功能
3.增加文章收藏订阅功能，用户可以第一时间收到订阅消息
4.增加文章搜索功能，可以根据文章标题和内容进行模糊查询
5.页面美化

备注：项目界面截图在文件夹Image里面

环境：
1. python2.7/python3.4
2. mysql5.5+
3. Reference: Flask Web开发-基于Python的Web应用开发实战

Start：
  $pip install -r requirements/dev.txt

Run Mysql、redit and celery:
	$service redis start

	$service mysqld start

	$celery worker -A celery_worker.celery -l INFO &
	
Create testdata and upgrade to mysql: 
	$ python manage.py db init

	$ python manage.py db migrate
	
	$ python manage.py db upgrade

	$ python manage.py datainit

	$ python manage.py runserver

主页: http://127.0.0.1:5000/
