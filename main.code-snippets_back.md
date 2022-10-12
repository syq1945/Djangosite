{
	// Place your 全局 snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and 
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope 
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is 
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are: 
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. 
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"main": {
		"prefix": "main",
		"body": [
			"if __name__ == '__main__':",
			"    app.run()"
		],
		"description": "template for the main"
	},
	
	"divclass": {
		"prefix": "divclass",
		"body": [
			"<div class=''></div>",
		],
		"description": "div with blank class"
	},

	"divcontai": {
		"prefix": "divcontai",
		"body": [
			"<div class=' container'>",
			"",
			"</div>"
		],
		"description": "div with container"
	},

	"titl": {
		"prefix": "titl",
		"body": [
			"{{ title }}"
		],
		"description": "占位符 {{ var }}"
	},

	"placeholders": {
		"prefix": "placeholders",
		"body": [
			"placeholder= ' ' "
		],
		"description": "placeholder= ' ' "
	},

	"inputtext": {
		"prefix": "inputtext",
		"body": [
			"<input type='text' class='' value=''  name='' placeholder= '' />"
		],
		"description": "<input type='text'... "
	},

	"div": {
		"prefix": "div",
		"body": [
			"<div class='' id=''> </div>  "
		],
		"description": "<div class=... "
	},

	"buttonprimary": {
		"prefix": "buttonprimary",
		"body": [
			"<button type=\"button\" class=\"btn btn-primary\"> 按钮名 </button>"
		],
		"description": "buttonprimary... "
	},

	"inputsubmit": {
		"prefix": "inputsubmit",
		"body": [
			"<input type='submit' class='' value='提 交'>"
		],
		"description": "<input type='submit'... "
	},

	"hr": {
		"prefix": "hr",
		"body": [
			"<hr/>"
		],
		"description": "<hr/> 一条横线"
	},

	
	"approutadduser": {
		"prefix": "approutadduser",
		"body": [
			"@app.route('/add/user', methods=['GET', 'POST'])       ",
			"def add_user():                                        ",
			"    if request.method == 'GET':                        ",
			"        return render_template('add_user.html')        ",
			"    else:                                              ",
			"        username = request.form.get('username')        ",
			"        pwd = request.form.get('pwd')                  ",
			"        mobile = request.form.get('mobile')            ",
			"        line_list = [username, pwd, mobile]            ",
			"                                                       ",
			"        insert_union_admin(line_list)                  ",
			"        return '添加成功'                              ",
			""
		],
		"description": "<input type='submit'... "
	},

	"formpostlogin": {
		"prefix": "formpostlogin",
		"body": [
			"<form class=\"form-inline\" method=\"post\" action=\"/info/add/\">                                                                              ",
			"  {% csrf_token %} ",
			"  <div class=\"form-group\">                                                                              ",
			"    <input type=\"text\" class=\"form-control\" id=\"\" name='username' placeholder= 'username'>          ",
			"  </div>                                                                                                  ",
			"  <div class=\"form-group\">                                                                              ",
			"    <input type=\"password\" class=\"form-control\" id=\"\" name='password' placeholder=\"Password\">     ",
			"  </div>                                                                                                  ",
			"  <button type=\"submit\" class=\"btn btn-primary\">Sign in</button>                                      ",
			"</form>                                                                                                   ",
			""
		],
		"description": "<form method=\"post\"... "
	},

	
	"formpostadd": {
		"prefix": "formpostadd",
		"body": [
			"<form class=\"form-inline\" method=\"post\" action=\"/info/add/\">                                                                              ",
			"  {% csrf_token %} ",
			"  <div class=\"form-group\">                                                                              ",
			"    <input type=\"text\" class=\"form-control\" id=\"\" name='department' placeholder= 'department'>          ",
			"  </div>                                                                                                  ",
			"  <div class=\"form-group\">                                                                              ",
			"    <input type=\"text\" class=\"form-control\" id=\"\" name='dept_num' placeholder=\"dept_num\">     ",
			"  </div>                                                                                                  ",
			"  <button type=\"submit\" class=\"btn btn-primary\">新 建</button>                                      ",
			"</form>                                                                                                   ",
			""
		],
		"description": "<form method=\"post\"... "
	},

		"ul": {
		"prefix": "ul",
		"body": [
			 "<ul>",
			 "",
			 "</ul>"
		],
		"description": "<ul... "
	},

	"li": {
		"prefix": "li",
		"body": [
			 "   <li>  </li>    "
		],
		"description": "<ul... "
	},

	"inputpassword": {
		"prefix": "inputpassword",
		"body": [
			 "<input type='password' class='' value=''  name='user' placeholder= 'password' />     "
		],
		"description": "<inputpassword... "
	},

	"CharField32": {
		"prefix": "CharField32",
		"body": [
			 "models.CharField(max_length=32)    "
		],
		"description": "=models.CharField(max_length=32) "
	},
	"CharField64": {
		"prefix": "CharField64",
		"body": [
			 "models.CharField(max_length=64)    "
		],
		"description": "=models.CharField(max_length=64) "
	},

	"IntegerField": {
		"prefix": "IntegerField",
		"body": [
			 "models.IntegerField()    "
		],
		"description": "=models.IntegerField()  "
	},

	"a": {
		"prefix": "a",
		"body": [
			 "<a target=\"_blank\" href=\"\" class=\"btn btn-primary btn-sm \">按钮名</a>  "
		],
		"description": "<a...  "
	},

	"adel": {
		"prefix": "adel",
		"body": [
			 "<a  href=\"/info/del/?nid={{item.id}}\" class=\"btn btn-danger btn-xs \">删除</a>  "
		],
		"description": "<a...  "
	},

	"aedit": {
		"prefix": "aedit",
		"body": [
			 "<a href=\"/info/edit/?nid={{item.id}}\" class=\"btn btn-primary btn-xs \">编辑</a>  "
		],
		"description": "<a...  "
	},

	"BooleanField": {
		"prefix": "BooleanField",
		"body": [
			 "models.BooleanField()    "
		],
		"description": "=models.BooleanField()  "
	},

	"newdjango": {
		"prefix": "newdjango",
		"body": [
			"{% load static %}  ",                                                                         
			"<!DOCTYPE html>                                                                             ",
			"<html lang='en'>                                                                            ",
			"  <head>                                                                                    ",
			"    <meta charset='UTF-8' />                                                                ",
			"    <title>Title</title>                                                                    ",
			"    <!-- https://v3.bootcss.com/ -->                                                        ",
			"    <link                                                                                   ",
			"      rel='stylesheet'                                                                      ",
			"      href=\"{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}\"                       ",
			"    />                                                                                      ",
			"    <!-- https://fontawesome.dashgame.com -->                                               ",
			"    <link                                                                                   ",
			"      rel='stylesheet'                                                                      ",
			"      href=\"{% static 'plugins/font-awesome-4.7.0/css/font-awesome.css' %}\"                 ",
			"    />                                                                                      ",
			"                                                                                            ",
			"    <style>                                                                                 ",
			"      .navbar {                                                                             ",
			"        border-radius: 0px;                                                                 ",
			"      }                                                                                     ",
			"    </style>                                                                                ",
			"  </head>                                                                                   ",
			"                                                                                            ",
			"  <body>                                                                                    ",
			"    <!--html从这里开始写 -->    <!--class=\"container\" 可以让内容居中 ; class=\"container-fluid\" 让内容顶格 -->                                                                    ",
			"                                                                                            ",
			"    <h1>!用户列表!:</h1>     ",
			"    <h2>                                                                            ",
			"      <ul>                                                                      ",
			"        {% for dict in data_list %}  <!--Django 使用for循环,显示data_list 中 dict的内容-->    ",
			"        <li>                                                                    ",
			"          Name: {{dict.name}} ; Role: {{dict.role}} ; Salary: {{dict.salary}}   ",
			"        </li>                                                                   ",
			"        {% endfor %}                                                            ",
			"      </ul>                                                                     ", 
			"      <hr/>                                                                        ",
			"      {% if name == \"Terry Sun\"  %}   <!--Django 使用if-else语句-->                  ",
			"      <h1> yesyesyes \"Terry Sun\" </h1>    <!--Django == 和 \"\" 中间要有空格-->           ",
			"      {% elif name == \"Terry Sun_LM\" %}                                          ",
			"      <h1> yesyesyes \"Terry Sun_LM\" </h1>                                        ",
			"      {% else %}                                                                   ",
			"        <h1> nonono</h1>                                                           ",
			"      {% endif %}                                                                  ",
			"    </h2>                                  ",
			"    <img src=\"{% static 'img/blade.jpg' %}\" alt='' />      ", 
			"                                                                                            ",
			"    <!-- https://jquery.com/ -->                                                            ",
			"    <script src=\"{% static 'js/jquery-3.6.1.min.js' %}\"></script>                           ",
			"    <!-- https://jquery.com/ 引入bootstrap的js -->                                             ",
			"    <script src=\"{% static 'plugins/bootstrap-3.4.1/js/bootstrap.min.js' %}\"></script>      ", 
			"                                                                                            ",
			"    <!-- Javascript代码推荐位置: -->                                                              ",
			"    <script type='text/javascript'>                                                         ",
			"      //利用jQuery中的功能实现某些效果                                                                  ",
			"      //框架启动后, 就能运行的代码, 不用等所有都加载完, 可以节省些时间                                                  ",
			"      $(function () {});                                                                    ",
			"    </script>                                                                               ",
			"  </body>                                                                                   ",
			"</html>                                   login                                                  ",
			"                                                                                            ",
			" "
		],
		"description": "newdjango_html_file... "
	},

	"anzhuangDjango": {
		"prefix": "anzhuangDjango",
		"body": [
			"##   https://www.cnblogs.com/wupeiqi   老师的博客园, 有很多可以学些的知识  ",
			"# # vscode 运行虚拟环境 virtualenv 时报错：'_Scripts_Activate.ps1'，因为在此系统上禁止运行脚本       ",
			"                                                                                                   ",
			"# 解决方法：                                                                                       ",
			"# win+x点击Windows PowerShell（管理员）                                                            ",
			"                                                                                                   ",
			"#  'set-executionpolicy remotesigned'  输入这个命令允许允许脚本",
			"                                                                                                   ",
			"# # 在本项目文件夹内创建虚拟环境                                                                   ",
			"                                                                                                   ",
			"# 'python -m venv env'  # 创建环境, 文件夹名为env ",
			" # .\\env\\scripts\\activate  # 用向右向下斜杠替换_激活虚拟环境",
			"# 'pip install django==2.2.5 -i https://pypi.douban.com/simple '  # 安装Django稳定版                                                                   ",
			"# 'Python -m pip install --upgrade pip'  # 升级pip                                                   ",
			"# 'pip install pymysql  -i https://pypi.douban.com/simple' ",
			"#  'pip install pandas  -i https://pypi.douban.com/simple' ",
			"#  'pip install mysqlclient==2.1.0  -i https://pypi.douban.com/simple' ",
			"#  django-admin startproject Djangosite . #这里的空格+.表示在当前文件夹下来创建项目并把manage.py放在跟目录下",
			"#  python manage.py startapp APP_UserManage  # 创建一个APP -用向右向下斜杠替换_    ",
			"# [settings]中注册 - 在 installed_app=[ 下增加 'APP_UserManage.apps.AppUsermanageConfig', 可以在APP_UserManage文件夹下apps.py中找到相关类的名称",
			"# [urls] 中增加 from APP_UserManage import views  并在urlpatterns=[ 下增加 path('index/', views.index),  ",
			"# [views]中创建index函数 - 至此浏览器中就能有些内容了",
			"# [views]中 修改和增加 ",
			"#from django.shortcuts import render,HttpResponse,redirect                                      ",
			"#from APP_UserManage import models                                                              ",
			"#                                                                                               ",
			"#                                                                                               ",
			"## class MyForm(ModelForm):                                                                     ",
			"##     class Meta:                                                                              ",
			"##         model =Department                                                                    ",
			"##         fields=[\"deparment\",\"dep_number\"]                                                ",
			"#                                                                                               ",
			"#def index(request):                                                                            ",
			"#    return render(request,'index.html')                                                        ",
			"#                                                                                               ",
			"#def dept_list(request):                                                                        ",
			"#    data_list=models.Department.objects.all()                                                  ",
			"#    if request.method== \"GET\":                                                               ",
			"#        return render(request,'dept_list.html',{\"data_list\":data_list})                      ",
			"#    # 从frompost中获取a标签中 name=\"xxx\"的值                                                          ",
			"#    deparment=request.POST.get(\"deparment\")                                                  ",
			"#    dep_number=request.POST.get(\"dep_number\")                                                ",                                                       
			"#    #添加到数据库                                                                                    ",
			"#    models.Department.objects.create(deparment=deparment,dep_number=dep_number)                ",
			"#    #跳转到用户列表界面                                                                                 ",
			"#    return redirect(\"/dept/list/\")                                                           ",
			"#                                                                                               ",
			"#def dept_del(request):  #删除功能 -   # href=\"/dept/del/?nid={{item.id}}\" 来实现                                  ", 
			"#    nid=request.GET.get(\"nid\")                                                               ",
			"#    models.Department.objects.filter(id=nid).delete()                                          ",
			"#    return redirect(\"/dept/list/\")                                                           ",
			"#                                                                                               ",
			"#def dept_edit(request):     #编辑功能 -    # href=\"/dept/del/?nid={{item.id}}\" 来实现                             ",   
			"#    nid=request.GET.get(\"nid\")                                                               ",
			"#    deparment=request.GET.get(\"deparment\")                                                   ",
			"#    dep_number=request.GET.get(\"dep_number\")                                                 ",
			"#    models.Department.objects.filter(id=nid).update(deparment=deparment,dep_number=dep_number) ",   
			"#    return redirect(\"/dept/list/\")                                                           ",
			"",
			"",
			"",
			"# [Model]",
			"#from django.db import models                                                                                                                  ",
			"# #先录入部门表, 之后员工表, 之后Region表,之后工厂表                                                                                                                                              ",
			"#class Department(models.Model):                                                                                                               ",
			"#    '''部门表'''                                                                                                                                 ",
			"#    deparment=models.CharField(verbose_name=\"部门名称\",max_length=32)                                                                           ",
			"#    dep_number=models.IntegerField(verbose_name=\"部门号\")                                                                                      ",
			"#    # pwd=models.CharField(max_length=64)                                                                                                     ",
			"#    # age=models.IntegerField(null=True,blank=True)  #允许为空, 允许不填                                                                              ",
			"#    # del_flag=models.BooleanField(verbose_name=\"删除标记\",default=0,null=True,blank=True)  # 默认值为0, #允许为空, 允许不填                                ",
			"#                                                                                                                                              ",
			"#class Factory(models.Model):                                                                                                                  ",
			"#    '''工厂表'''                                                                                                                                 ",
			"#    factory=models.CharField(verbose_name=\"工厂名\",max_length=32)                                                                              ",
			"#    factory_d_ID=models.BigIntegerField(verbose_name=\"厂长用户ID\")                                                                              ",
			"#    finance_manager_ID=models.BigIntegerField(verbose_name=\"财务经理用户ID\")                                                                      ",
			"#    sourcing_manager_ID=models.BigIntegerField(verbose_name=\"采购经理用户ID\")                                                                     ",
			"#    region_ID=models.BigIntegerField(verbose_name=\"Region_ID\")                                                                              ",
			"#                                                                                                                                              ",
			"#class Region(models.Model):                                                                                                                   ",
			"#    '''Region management Team表'''                                                                                                             ",
			"#    region=models.CharField(verbose_name=\"工厂名\",max_length=32)                                                                               ",
			"#    re_vp_id=models.BigIntegerField(verbose_name=\"Region_VP_ID\")                                                                            ",
			"#    re_finance_d_id=models.BigIntegerField(verbose_name=\"Region_FinanceD_ID\")                                                               ",
			"#    re_sourcing_d_id=models.BigIntegerField(verbose_name=\"Region_SourcingD_ID\")                                                             ",
			"#    re_capex_d_id=models.BigIntegerField(verbose_name=\"Region_HRD_ID\")                                                                      ",
			"#    re_hr_d_id=models.BigIntegerField(verbose_name=\"Region_HRD_ID\")                                                                         ",
			"#    re_IT_d_id=models.BigIntegerField(verbose_name=\"Region_ITD_ID\")                                                                         ",
			"#                                                                                                                                              ",
			"#class UserInfo(models.Model):                                                                                                                 ",
			"#    '''员工表'''                                                                                                                                 ",
			"#                                                                                                                                              ",
			"#    username=models.CharField(verbose_name=\"姓名\",max_length=32)                                                                              ",
			"#    password=models.CharField(verbose_name=\"标题\",max_length=64)                                                                              ",
			"#    gender_choices=((1,\"男\"),(0,\"女\"))                                                                                                      ",
			"#    gender=models.SmallIntegerField(verbose_name=\"性别\",choices=gender_choices)                                                               ",
			"#    account=models.DecimalField(verbose_name=\"账户余额\",max_digits=19,decimal_places=4,default=0,null=True,blank=True)                          ",
			"#    manager=models.CharField(verbose_name=\"people leader\",max_length=32)                                                                    ",
			"#    create_time=models.DateTimeField(verbose_name=\"入职时间\")                                                                                   ",
			"#    edit_time=models.DateTimeField(verbose_name=\"修改时间\",null=True,blank=True)                                                                ",
			"#    departmen=models.ForeignKey(to=\"Department\", to_field=\"id\",on_delete=models.SET_NULL,null=True,blank=True,verbose_name=\"部门ID\")      ",
			"#    # department_ID=models.BigIntegerField(verbose_name=\"部门ID\")                                                                             ",
			"#    permission=models.CharField(verbose_name=\"权限\",max_length=32,null=True,blank=True)                                                       ",
			"#    del_flag=models.BooleanField(verbose_name=\"删除标记\",default=0,null=True,blank=True)  # 默认值为0, #允许为空, 允许不填   ",
			"",
			"",			
			"#   [Django ORM:]",
			"#   CREATE DATABASE YourDBName DEFAULT CHARSET utf8mb4 ; ",			
			"# [settings] - DATABASE={ ..中替换成MySQL的设置 ",
			"#DATABASES = {                              ", 
			"#    'default': {                           ",
			"#    'ENGINE': 'django.db.backends.mysql',  ",
			"#    'NAME':'YourDBName',   #改成创建的数据库名    ",
			"#    'USER': 'root',                        ",
			"#    'PASSWORD': 'LM-china1',               ",
			"#    'HOST': '127.0.0.1',                   ",
			"#    'PORT': '3306',                        ",
			"#    }                                      ",
			"#}   ",  
			"#   运行终端时, 确定运行的是自己文件夹得终端",
			"#   python manage.py makemigrations  #ORM初始化 ",
			"#   python manage.py migrate  #创建数据表",
			"#   python manage.py runserver  ",
			"#   python manage.py createsuperuser    # admin lm-china1  在/admin 中使用",
			"",
			"# [admin] 中增加:  实现在/admin中增加相关部分",
			"#   from .models import UserInfo,Department ",
			"",
			"#   class UserInfoAdmin(admin.ModelAdmin):",
			"#       list_display=(\"username\",\"pwd\",\"age\",\"del_flag\")",
			"#   ",
			"#   class DepartmentAdmin(admin.ModelAdmin):",
			"#       list_display=(\"title\",)",
			"#                                           ",
			"#   admin.site.register(UserInfo,UserInfoAdmin)           ",
			"#   admin.site.register(Department,DepartmentAdmin)         ",
			"",
			"# [ModelForm] ",
			"",
			"",
			"",
			"",
			"",
			"",
			"#[models]中 创建表类 没有写ID, Django会自动创建主键: id BIGINT PRIMARY KEY AUTO_INCREMENT, ",
			"#class UserInfo(models.Model):                                                       ",
			"#  '''用户表'''",
			"#    username=models.CharField(verbose_name=\"用户名\",max_length=32)                                        ",
			"#    pwd=models.CharField(verbose_name=\"密码\",max_length=64)                                             ",
			"#    age=models.IntegerField(verbose_name=\"年龄\",null=True,blank=True)  #允许为空, 允许不填                    ",
			"#    del_flag=models.BooleanField(verbose_name=\"删除标志\",default=0,null=True,blank=True)  # 默认值为0, #允许为空, 允许不填                              ",
			"#    title=models.CharField(verbose_name=\"标题\",max_length=16)                                           ",
			"#    news_title=models.CharField(verbose_name=\"新闻标题\",max_length=255)",
			"#    url=models.CharField(verbose_name=\"URL\",max_length=2083)",
			"#    account=models.DecimalField(verbose_name=\"账户余额\",max_digits=19,decimal_places=4,default=0,null=True,blank=True)",
			"#    create_time=models.DateTimeField(verbose_name=\"入职时间\")",
			"#    edit_time=models.DateTimeField(verbose_name=\"修改时间\",null=True,blank=True)",
			"#    permission=models.CharField(verbose_name=\"权限\",max_length=32) ",
			"#    gender_choices=((1,\"男\"),(0,\"女\")) ",
			"#    gender=models.SmallIntegerField(verbose_name=\"性别\",choices=gender_choices)  ",
			"#    departmen=models.ForeignKey(to=\"Department\", to_field=\"id\",on_delete=models.SET_NULL,null=True,blank=True,verbose_name=\"部门ID\")    ",
			"##    department_ID=models.BigIntegerField(verbose_name=\"部门ID\")",
			"#                                                                                       ",
			"##   UserInfo.objects.create(username=\"tsu\",pwd=\"lm-china1\")  # 新建                       ",
			"##   UserInfo.objects.create(username=\"admin\",pwd=\"lm-china1\")   # 新建                     ",
			"##   # 新建数据   自动生成:  insert into app01_department(title) vlaues(\"销售部\")                 ",
			"##   Department.objects.create(title=\"销售部\")   # 新建                                          ",
			"#   ",
			"##   UserInfo.objects.filter(id=4).delete()  # 删除按钮的功能",
			"##   Department.objects.all().delete()  # 清空表",
			"#   ",
			"##   data_list=UserInfo.objects.all()  # 获取表所有内容",
			"##   for obj in data_list:",
			"##     print(obj.id, obj.username, obj.pwd,obj.age, obj.del_flag)",
			"#   ",
			"##   row_obj=UserInfo.objects.filter(id=1).first()  # 获取一行数据",
			"##   print(row_obj.id,row_obj.username,row_obj.pwd,row_obj.age,row_obj.del_flag)",
			"#   ",
			"##   UserInfo.objects.create(username=\"tsu\",pwd=\"lm-china1\")  # 新建数据 ",
			"##   UserInfo.objects.filter(id=1).update(pwd=\"123\")  #修改数据",
			"##   UserInfo.objects.filter(id=2).update(del_flag=1)  # 删除数据",
			"#   ",
			"#   ",
			"#  django-admin startproject Djangosite . #这里的空格+.表示在当前文件夹下来创建项目并把manage.py放在跟目录下",
			"#  python manage.py startapp app01# 创建一个APP -用向右向下斜杠替换_",
			"# [settings] 中注册 - 在 installed_app=[ 下增加 'app01.apps.App01Config', 可以在app01文件夹下apps.py中找到相关类的名称",
			"# [urls] 中增加 from app01 import views  并在urlpatterns=[ 下增加 path('index/', views.index), ",
			"# [views] 中创建index函数 - 至此浏览器中就能有些内容了",
			"# [views] 中 from django.shortcuts import render,HttpResponse,redirect",
			"def user_list(request):                   ",
			"  #1. 获取数据库中所有用户的信息",
			"  data_list=UserInfo.objects.filter(del_flag=0)",
			"  #2. 渲染, 返回给用户",
			"  return render(request,'user_list.html', {\"data_list\":data_list}) ",
			"# def index(request):              ",
			"#  return HttpResponse('欢迎使用')",
			"# def redirecttomytechchart(request):              ",
			"#  return redirect(\"https://geit.service-now.com/mytech_support_chat.do\")",
			"",
			"def info_add(request):                                         ",
			"  if request.method== \"GET\":                                 ",
			"    return render(request,'info_add.html')                     ",
			"  # 获取用户提交的数据                                                  ",
			"  username=request.POST.get(\"username\")                      ",
			"  pwd=request.POST.get(\"pwd\")                                ",
			"  age=request.POST.get(\"age\")                                ",
			"  del_flag=request.POST.get(\"del_flag\")                      ",
			"                                                               ",
			"  #添加到数据库                                                      ",
			"  UserInfo.objects.create(username=username,pwd=pwd,age=age)   ",
			"  #跳转到用户列表界面                                                   ",
			"  return redirect(\"/info/list/\")                             ",
			"",
			"  #删除功能 - 通过修改del_flag实现   # href=\"/info/del/?nid={{item.id}}\" 来实现 ",
			"  def info_del(request):                                  ",
			"    nid=request.GET.get(\"nid\")                            ",
			"    UserInfo.objects.filter(id=nid).update(del_flag=1)    ",
			"    return redirect(\"/info/list/\")                        ",
			"",
			"",
			"",
			"",
			"",
			"",
			"# 启动Django - python manage.py runserver  ",
			"# [urls] 中新加第二个页面 path('user/list', views.user_list), # 前面式url后缀, 后面views.是views.py中的函数名称",
			"# [views] 中创建index函数user_list:  def user_list(request):   return render(request,'user_list.html')",
			"  #默认情况下,在app的先后顺序去找.         ",
			"  # 先去在app01 templates文件夹中找这个文件   ",
			"  # 再去  app02 templates文件夹中找这个文件   ",
			"# def tpl(request):                                                                                                      ",           
			"#   name=\"Terry Sun\"                                                                                                   ",
			"#   roles=[\"admin\",\"CEO\",\"China\"]                                                                                  ",
			"#   user_dict={\"name\":\"郭志\",\"salary\":100000,\"role\":\"CEO\"}                                                       ",
			"#   data_list=[                                                                                                          ",
			"#     {\"name\":\"郭志\",\"salary\":100000,\"role\":\"CEO\"} ,                                                             ",
			"#     {\"name\":\"张三\",\"salary\":200000,\"role\":\"CTO\"} ,                                                             ",
			"#     {\"name\":\"李四\",\"salary\":300000,\"role\":\"CFO\"} ,                                                             ",
			"#     {\"name\":\"王五\",\"salary\":400000,\"role\":\"VP\"}                                                                ",
			"#   ]                                                                                                                    ",
			"#   # Django 使用字典的方式传参数 {\"Key1\":data1,\"key2\":data2}                                                                  ",
			"#   return render(request,'tpl.html',{\"name\":name,\"roles\":roles,\"user_dict\":user_dict,\"data_list\":data_list})    ",
			"# python manage.py migrate ",
			"",
			"",
			"",
			"",
			""
		],
		"description": "anzhuangDjango..."
	},

		"tablefor": {
		"prefix": "tablefor",
		"body": [
			"<table class='table table-hover table-striped table-bordered'>         ",
			"      <thead>                                                      ",
			"        <tr>                                                       ",
			"          <th>ID</th>                                              ",
			"          <th>用户名</th>                                             ",
			"          <th>密码</th>                                              ",
			"          <th>手机号</th>                                             ",
			"          <th>操作</th> ",
			"        </tr>                                                      ",
			"      </thead>                                                     ",
			"      <tbody>                                                      ",
			"        {% for item in data_list %}                                ",
			"        <tr>                                                       ",
			"          <th scope='row'>{{item.id}}</th>                         ",
			"          <td>{{item.username}}</td>                               ",
			"          <td>{{item.pwd}}</td>                                    ",
			"          <td>{{item.mobile}}</td>                                 ",
			"          <th><a href=\"/info/edit/?nid={{item.id}}\" class=\"btn btn-success btn-xs \">编辑</a>  <a  href=\"/info/del/?nid={{item.id}}\" class=\"btn btn-danger btn-xs \">删除</a>  </th> ",
			"        </tr>                                                      ",
			"        {% endfor %}                                               ",
			"        </tbody> ",
			"      </table>   ",
			""
		],
		"description": "<table with for... "
	},


	"table": {
		"prefix": "table",
		"body": [
			"<table class=\"table table-striped\">    ",
			"  <thead>                  ",
			"    <tr>                   ",
			"      <th></th>            ",
			"      <th></th>            ",
			"    </tr>                  ",
			"  </thead>                 ",
			"  <tbody>                  ",
			"    <tr>                   ",
			"      <td></td>            ",
			"      <td></td>            ",
			"    </tr>                  ",
			"  </tbody>                 ",
			"</table>                   ",
			""
		],
		"description": "<table... "
	},

	"newhtml": {
		"prefix": "newhtml",
		"body": [
			"<!DOCTYPE html>",
			"<html lang='en'>",
			"",
			"<head>",
			"    <meta charset='UTF-8' />",
			"    <title>Title</title>",
			"    <!-- https://v3.bootcss.com/ -->",
			"    <link rel='stylesheet' href='/static/plugins/bootstrap-3.4.1/css/bootstrap.css' />",
			"    <!-- https://fontawesome.dashgame.com -->",
			"    <link rel='stylesheet' href='/static/plugins/font-awesome-4.7.0/css/font-awesome.css' />",
			"    <!-- <link rel='stylesheet' href='/static/css/style.css'> -->",
			"    <!-- <link rel='stylesheet' href='/static/css/tvshowpic.css' /> -->",
			"",
			"    <style>",
			"        .navbar {",
			"            border-radius: 0px;",
			"        }",
			"    </style>",
			"</head>",
			"",
			"<body>",
			"    <!--html从这里开始写 --> ",
			"    <!--class=\"container\" 可以让内容居中 ; class=\"container-fluid\" 让内容顶格 -->",
			"",
			"",
			"",
			"    <!-- https://jquery.com/ -->",
			"    <script src='/static/js/jquery-3.6.1.min.js'></script>",
			"    <!-- https://jquery.com/ 引入bootstrap的js -->",
			"    <script src='/static/plugins/bootstrap-3.4.1/js/bootstrap.min.js'></script>",
			"",
			"    <!-- Javascript代码推荐位置: -->",
			"    <script type='text/javascript'>",
			"        //利用jQuery中的功能实现某些效果",
			"        //框架启动后, 就能运行的代码, 不用等所有都加载完, 可以节省些时间",
			"        $(function ()",
			"        {",
			"",
			"",
			"        })",
			"    </script>",
			"",
			"",
			"</body>",
			"",
			"</html>",
			""
		],
		"description": "template for new html file"
	},

	"flask": {
		"prefix": "flask",
		"body": [
			"from flask import Flask, render_template",
			"",
			"app = Flask(__name__)",
			"",
			"",
			"@app.route('/index')",
			"def index():",
			"    return render_template('index.html')",
			"",
			"",
			"if __name__ == '__main__':",
			"    app.run()",
			""
		],
		"description": "template for new flask app.py"
	},

	"importpymysql": {
		"prefix": "import pymysql",
		"body" : [
			"#  pip install pymysql                                                         ",    
			"#  pip install pandas                                                          ",
			"                                                                               ",
			"import pymysql                                                                 ",
			"import pandas as pd                                                            ",
			"                                                                               ",
			"__author__ = 'Terry Sun'                                                       ",
			"                                                                               ",
			"host = '127.0.0.1'                                                             ",
			"user = 'root'                                                                  ",
			"passwd = 'LM-china1'                                                           ",
			"db = 'unicom'                                                                  ",
			"port = 3306                                                                    ",
			"charset = 'utf8'                                                               ",
			"                                                                               ",
			"# 二维数组                                                                         ",
			"# update_data = [                                                              ",
			"#     [81, 1],                                                                 ",
			"#     [90, 2],                                                                 ",
			"#     [72, 3]                                                                  ",
			"# ]                                                                            ",
			"                                                                               ",
			"#   user=' '                                                                    ",
			"# password=' '                                                                  ",
			"# mobile=' '                                                                    ",
			"#[user, password,mobile]                                                       ",
			"                                                                               ",
			"                                                                               ",
			"#  ctrl+shift +L 可以批量修改名字                                                      ",
			"                                                                               ",
			"db = pymysql.connect(host=host, port=port, user=user,                          ",
			"                     passwd=passwd, db=db, charset=charset)                    ",
			"cursor = db.cursor(cursor=pymysql.cursors.DictCursor)                          ",
			"                                                                               ",
			"# # ===========================                                                ",
			"# # insert 部分开始                                                                ",
			"# #修改多行数据                                                                      ",
			"# excel_path = r'admin.xlsx'                                                   ",
			"# df = pd.read_excel(excel_path)                                               ",
			"# df_list = df.values.tolist()                                                 ",
			"# insert_sql = 'INSERT INTO admin(username,pwd,mobile) VALUES(%s,%s,%s); '    ",
			"# cursor.executemany(insert_sql, df_list)                                      ",
			"#                                                                              ",
			"# # 修改一行数据                                                                     ",
			"# # insert_sql = 'INSERT INTO admin(username,pwd,mobile) VALUES(%s,%s,%s); '     ",
			"# # line_list=['lx001','LM8888@ge','15912345678']                                ",
			"# # cursor.execute(insert_sql, line_list)                                        ",
			"## insert 部分结束                                                                  ",
			"# # ===========================                                                ",
			"# # ===========================                                                ",
			"# # select部分开始                                                                 ",
			"# select_sql = 'select * from admin where del_flag=0;'                         ",
			"# # cursor的execute 函数, 执行SQL                                                   ",
			"# cursor.execute(select_sql)                                                   ",
			"# # cursor的fetchall函数, 获取得到的类型为list, 元素内部为字典的 数据                               ",
			"# data_list = cursor.fetchall()                                                ",
			"# # fetchone() 的类型是dict, 只获取一行数据                                               ",
			"# #data_list1 = cursor.fetchone()                                              ",
			"# print(type(data_list))                                                       ",
			"# # 遍历 list, 得到每一个字典数据.                                                        ",
			"# for data_dict in data_list:                                                  ",
			"#     print(data_dict)                                                         ",
			"#                                                                              ",
			"# # select部分结束                                                                 ",
			"# # ===========================                                                ",
			"# # ===========================                                                ",
			"# #update部分开始                                                                   ",
			"# excel_path = r'update.xlsx'                                                  ",
			"# df = pd.read_excel(excel_path)                                               ",
			"# df_list = df.values.tolist()                                                 ",
			"# # df_list=[  [1,1],[1,2] ]                                                    ",
			"# #修改多行数据                                                                       ",
			"# update_sql = 'update admin set del_flag=%s   where id=%s;'                   ",
			"# cursor.executemany(update_sql, df_list)                                      ",
			"                                                                               ",
			"###  修改一行数据                                                                     ",
			"# # update_sql = 'update admin set del_flag=%s   where id=%s;'                   ",
			"# # line_list=[1,4]                                                              ",
			"# # cursor.execute(update_sql, line_list)                                        ",
			"                                                                               ",
			"### update部分结束                                                                   ",
			"# # ===========================                                                ",
			"                                                                               ",
			"db.commit()                                                                    ",
				"                                                                               ",
				"cursor.close()                                                                 ",
				"db.close()                                                                     ",
				"                                                                               "
		],
		"description": "MySQL.py 框架"
	}
}

	
