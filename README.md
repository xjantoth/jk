
# First Docerized App: jk
# navigate to working directory
```
cd /tmp
git clone this-project
mkdir /opt/workspace 
rsync -avhx /tmp/this-project/* /opt/workspace/ 
cd /opt/workspace
```


# list all files present in: "/opt/workspace"
```
ls -al  
drwxr-xr-x 4 root root 4096 Dec  4 12:30 .
drwxr-xr-x 6 root root 4096 Dec  2 06:54 ..
-rw-r--r-- 1 root root  161 Dec  2 07:14 docker-compose.yml
-rw-r--r-- 1 root root  544 Dec  4 12:30 Dockerfile
drwxr-xr-x 8 root root 4096 Dec  4 12:35 .git
drwxr-xr-x 8 root root 4096 Dec  4 12:31 jk
-rw-r--r-- 1 root root  521 Dec  4 10:34 jk_app.conf
-rw-r--r-- 1 root root  451 Dec  4 11:37 reqirements.txt
-rwxr-xr-x 1 root root  563 Dec  4 12:29 start_gunicorn.sh
-rw-r--r-- 1 root root 1130 Dec  4 09:45 supervisord.conf
```

# build an image
```
docker build -t "django:jk" .
```

# run docker for the first time
```
docker run -v /opt/workspace:/code  --name prototype -d --net=host  django:jk
```

# list processess
docker ps 
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
dac1b8de7c76        django:jk           "/code/start_gunic..."   3 seconds ago       Up 2 seconds                            prototype
```

# view logs 
```
docker logs  dac1b8de7c767646c7e422beecaf0df145ae160ed086e322ec4ad0f12718b229
```

