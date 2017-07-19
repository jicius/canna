###### 项目描述

> ?


###### 主要功能

1. ?
2. ?
3. ?


###### 快速开始

> 项目部署

    fab deploy_testing/deploy_production

> 创建supervisor conf 文件

    ; XXX服务
    [program:?_server]
    directory=/usr/local/?/current
    command=uwsgi config.ini
    autostart=true
    user=root
    redirect_stderr=true
    stdout_logfile=/var/log/?.log


> 启动服务

    supervisorctl reload


###### 协议说明

BSD