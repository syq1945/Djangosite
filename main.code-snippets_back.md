{ // Place your 全局 snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and // description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope // is left empty or omitted, the snippet gets applied to all languages. The prefix is what is // used to trigger the snippet and the body will be expanded and inserted. Possible variables are: // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. // Placeholders with the same ids are connected. // Example: // "Print to console": { // "scope": "javascript,typescript", // "prefix": "log", // "body": [ // "console.log('$1');", // "$2" // ], // "description": "Log output to console" // } "main": { "prefix": "main", "body": [ "if __name__ == '__main__':", " app.run()" ], "description": "template for the main" }

    "divclass": {
    	"prefix": "divclass",
    	"body": [
    		"<div class=' '></div>"
    	],
    	"description": "div with blank class"
    }

    "divcontai": {
    	"prefix": "divcontai",
    	"body": [
    		"<div class=' container'>",
    		"",
    		"</div>"
    	],
    	"description": "div with container"
    }

    "titl": {
    	"prefix": "titl",
    	"body": [
    		"{{ title }}"
    	],
    	"description": "占位符 {{ var }}"
    }

    "placeholders": {
    	"prefix": "placeholders",
    	"body": [
    		"placeholder= ' ' "
    	],
    	"description": "placeholder= ' ' "
    }

    "inputtext": {
    	"prefix": "inputtext",
    	"body": [
    		"<input type='text' class=' ' value=' '  name=' ' placeholder= ' ' />"
    	],
    	"description": "<input type='text'... "
    }

    "div": {
    	"prefix": "div",
    	"body": [
    		"<div class='' id=''> </div>  "
    	],
    	"description": "<div class=... "
    }

    	"buttonprimary": {
    	"prefix": "buttonprimary",
    	"body": [
    		"<button type=\"button\" class=\"btn btn-primary\"> 按钮名 </button>"
    	],
    	"description": "buttonprimary... "
    }

    "inputsubmit": {
    	"prefix": "inputsubmit",
    	"body": [
    		"<input type='submit' class=' ' value='提 交'>"
    	],
    	"description": "<input type='submit'... "
    }

    	"hr": {
    	"prefix": "hr",
    	"body": [
    		"<hr/>"
    	],
    	"description": "<hr/> 一条横线"
    }


    "approutadduser": {
    	"prefix": "approutadduser",
    	"body": [
    		"@app.route('/add/user', methods=['GET', 'POST'])		",
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
    }

    "form": {
    	"prefix": "form",
    	"body": [
    		 "   <form>    ",
    		"             ",
    		"   </form>   ",
    		""
    	],
    	"description": "<form... "
    }

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
    		"    <!--html从这里开始写 -->                                                                      ",
    		"                                                                                            ",
    		"    <h1>!用户列表!:</h1>     ",
    		"    <h2>                                                                            ",
    		"      <div class=\" \">{{name}}</div>   <!--Django 调用传进的字典参数-->                                               ",
    		"      <div class=\"\">{{roles.0}}</div>  <!--Django 使用字典的特殊格式-->                    ",
    		"      <div class=\"\">{{roles.1}}</div>                                             ",
    		"      <div class=\"\">{{roles.2}}</div>                                             ",
    		"      <div class=\"\" id=\"\">                                                      ",
    		"        {% for item in roles %}     <!--Django 使用for循环,显示列表中的内容-->                                                  ",
    		"        <div>{{item}}</div>                                                         ",
    		"        {% endfor %}                                                                ",
    		"      </div>   ",
    		"      <hr/>												",
    		"      {{user_dict}}                                         ",
    		"      <div class=\"\" id=\"\">{{user_dict.name}}</div>      ",
    		"      <div class=\"\" id=\"\">{{user_dict.salary}}</div>    ",
    		"      <div class=\"\" id=\"\">{{user_dict.role}}</div>  ",
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
    		"</html>                                                                                     ",
    		"                                                                                            ",
    		" "
    	],
    	"description": "newdjango_html_file... "
    }

    	"anzhuangDjango": {
    	"prefix": "anzhuangDjango",
    	"body": [
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
    		"#  django-admin startproject Djangosite . #这里的空格+.表示在当前文件夹下来创建项目并把manage.py放在跟目录下",
    		"#  python manage.py startapp app01# 创建一个APP -用向右向下斜杠替换_",
    		"# [settings.py]中注册 - 在 installed_app=[ 下增加 'app01.apps.App01Config', 可以在app01文件夹下apps.py中找到相关类的名称",
    		"# [urls.py] 中增加 from app01 import views  并在urlpatterns=[ 下增加 path('index/', views.index), ",
    		"# [views.py]中创建index函数 - 至此浏览器中就能有些内容了",
    		"# def index(request):              ",
    		"#  return HttpResponse('欢迎使用')",
    		"# 启动Django - python manage.py runserver  ",
    		"# [urls.py]中新加第二个页面 path('user/list', views.user_list), # 前面式url后缀, 后面views.是views.py中的函数名称",
    		"# [views.py]中创建index函数user_list:  def user_list(request):   return render(request,'user_list.html')",
    		"  #默认情况下,在app的先后顺序去找.         ",
    		"  # 先去在app01 templates文件夹中找这个文件   ",
    		"  # 再去  app02 templates文件夹中找这个文件   ",
    		"# def tpl(request):    # 传参数的写法                                                        ",
    		"#   name=\"Terry Sun\"                                                         ",
    		"#   roles=[\"admin\",\"CEO\",\"China\"]                                        ",
    		"#   return render(request,'tpl.html',{\"name\":name,\"roles\":roles})          ",
    		"# python manage.py migrate ",
    		"",
    		"",
    		"",
    		"",
    		""
    	],
    	"description": "anzhuangDjango..."
    }

    	"tablefor": {
    	"prefix": "tablefor",
    	"body": [
    		"<table class='table table-striped'>								",
    		"      <thead>                                                      ",
    		"        <tr>                                                       ",
    		"          <th>ID</th>                                              ",
    		"          <th>用户名</th>                                             ",
    		"          <th>密码</th>                                              ",
    		"          <th>手机号</th>                                             ",
    		"        </tr>                                                      ",
    		"      </thead>                                                     ",
    		"      <tbody>                                                      ",
    		"        {% for item in data_list %}                                ",
    		"        <tr>                                                       ",
    		"          <th scope='row'>{{item.id}}</th>                         ",
    		"          <td>{{item.username}}</td>                               ",
    		"          <td>{{item.pwd}}</td>                                    ",
    		"          <td>{{item.mobile}}</td>                                 ",
    		"        </tr>                                                      ",
    		"        {% endfor %}                                               ",
    		"        </tbody> ",
    		"      </table>   ",
    		""
    	],
    	"description": "<table with for... "
    }


    "table": {
    	"prefix": "table",
    	"body": [
    		"<table border='1'>			",
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
    }

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
    		"    <!--html从这里开始写 -->",
    		"",
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
    }

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
    }

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
