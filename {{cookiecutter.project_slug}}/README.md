# {{ cookiecutter.project_name }}

?


## Features

    ?


## Quick start

> Deploy

Configure fabfile before start your fab command.

    fab deploy_testing/deploy_production

> Create supervisor configure file

    ; {{ cookiecutter.project_name }}
    [program:{{ cookiecutter.project_name }}_server]
    directory=/usr/local/{{ cookiecutter.project_name }}/current
    command=uwsgi config.ini
    autostart=true
    user=root
    redirect_stderr=true
    stdout_logfile=/var/log/{{ cookiecutter.project_name }}.log


> 启动服务

    supervisorctl reload


###### 协议说明

BSD