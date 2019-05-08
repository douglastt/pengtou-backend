# Pengtou 项目代码结构
* `db.sqlite3`：sqlite数据库文件
* `src`：源码目录
    * `common`：项目全局文件目录
        * `settings.py`：项目设置
        * `urls.py`：项目路由
        * `wsgi.py`：django 内部文件
    * `pengtou`：pengtou 应用文件目录
        * `admin.py`：管理工具
        * `apps.py`：应用配置
        * `models.py`：模型
        * `tests.py`：测试
        * `urls.py`：应用路由
        * `views.py`：应用视图
* `etc`：其他文件目录
* `manage.py`：django 的命令行工具

# 启动
`python manage.py runserver`

# 请求示例
`http://127.0.0.1:8000/pengtou/testjson/`