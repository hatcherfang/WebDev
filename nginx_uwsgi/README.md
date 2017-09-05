# Usage  
- update file "myUwsgi.ini" about the directory "chdir = <pwd>"  
- start nginx   
`nginx -c <directory>/myNginx.conf`
- start uwsgi  
`uwsgi --ini <directory>/myUwsgi.ini`  
- input url:`http://ip` to visit the site  
# Reference   
- [uWSGI http和http-socket说明]("http://www.cnblogs.com/pengyusong/p/5780251.html")  
- uwsgi中 http 和 http-socket的使用上有一些区别:  
http: 自己会产生一个http进程(可以认为与nginx同一层)负责路由http请求给worker, http进程和worker之间使用的是uwsgi协议  
http-socket: 不会产生http进程, 一般用于在前端webserver不支持uwsgi而仅支持http时使用, 他产生的worker使用的是http协议  
因此, http 一般是作为独立部署的选项; http-socket 在前端webserver不支持uwsgi时使用,  
如果前端webserver支持uwsgi, 则直接使用socket即可(tcp or unix)  
