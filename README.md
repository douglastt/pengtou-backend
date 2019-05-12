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

# 接口

* User (示例)
    * 增
    
        `POST http://host:port/pengtou/user?nickname=n&avatar_url=a&gender=g&province=p&city=c&language=l`
    * 删 
    
        `DELETE http://host:port/pengtou/user?id=i`
    
    * 改（当post请求中包含id时视为更新操作，否则为新增操作）
    
        `POST http://host:port/pengtou/user?id=i&nickname=n&avatar_url=a&gender=g&province=p&city=c&language=l` 
    * 查
    
        `GET http://host:port/pengtou/user?id=i`
        
* Activity (示例)
    * 增
    
        `POST http://host:port/pengtou/activity?tag=t&address_final=a&time_on=2019-03-04 12:00:30&time_up=2019-03-04 12:30:30&is_finish=0`
    * 删 
    
        `DELETE http://host:port/pengtou/activity?id=i`
    
    * 改（当post请求中包含id时视为更新操作，否则为新增操作）
    
        `POST http://host:port/pengtou/user?id=i&tag=t&address_final=a&time_on=2019-03-04 12:00:30&time_up=2019-03-04 12:30:30&is_finish=0` 
    * 查
    
        `GET http://host:port/pengtou/activity?id=i`
        
* User activity (示例)
    * 增
    
        `POST http://host:port/pengtou/user_activity?user_id=ui&activity_id=ai&address_start=a&estimated_time=01:30:00&voting_id=vi`
    * 删 
    
        `DELETE http://host:port/pengtou/user_activity?user_id=ui&activity_id=ai`
    
    * 改（与增相同） 
    * 查
    
        `GET http://host:port/pengtou/user_activity?user_id=ui&activity_id=ai`
        
        
* Preferred location (示例)
    * 增
    
        `POST http://host:port/pengtou/preferred_location?type=t&name=n&location=l&score=s`
    * 删 
    
        `DELETE http://host:port/pengtou/preferred_location?id=i`
    
    * 改（当post请求中包含id时视为更新操作，否则为新增操作）
    
        `POST http://host:port/pengtou/preferred_location?id=i&type=t&name=n&location=l&score=s` 
    * 查
    
        `GET http://host:port/pengtou/preferred_location?id=i`
 
* Voting (示例)
    * 增
    
        `POST http://host:port/pengtou/voting?choose=c&num=n&address_id=ai`
    * 删 
    
        `DELETE http://host:port/pengtou/voting?id=i`
    
    * 改（当post请求中包含id时视为更新操作，否则为新增操作）
    
        `POST http://host:port/pengtou/voting?id=i&choose=c&num=n&address_id=ai` 
    * 查
    
        `GET http://host:port/pengtou/voting?id=i`
                