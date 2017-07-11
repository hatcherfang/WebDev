# Install apxs
- `yum install httpd-devel`
# Download file mod_uwsgi.c 
- `wget https://raw.githubusercontent.com/unbit/uwsgi/master/apache2/mod_uwsgi.c`
# Compile file mod_uwsgi.c
- `sudo apxs -i -a -c mod_uwsgi.c`
>> the file "mod_uwsgi.so" will be added in modules directory of apache server.
# Add string as below in apache configure file "httpd.conf" 
- `LoadModule uwsgi_module modules/mod_uwsgi.so`
# Update apache configure file "httpd.conf" 
- listen port 80 and redirect to 8001 port as below
  ```
  listen 80
  <VirtualHost *:80>
    ServerName 127.0.0.1
    ProxyPass / http://127.0.0.1:8001 
    ProxyPassReverse / http://127.0.0.1:8001
  </VirtualHost>
  ```
# Update myUwsgi.ini `chdir = <directory>` 
# Run command `uwsgi --ini myUwsgi.ini`

