#!/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#   Copyright (C) 2017 Jicius
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from fabric.api import env, run

project_name = '{{ cookiecutter.project_name }}'      # 项目名称
project_uri_testing = ""                              # 项目svn trunk 地址
project_uri_production = ""                           # 项目svn tags 地址

env.user = ""                                         # 远程登录用户名
env.hosts = []                                        # 远程登录主机
env.port = ""                                         # ssh 远程端口
env.password = ""                                     # 远程登录密码


def deploy_testing():
    run("cd /usr/local; mkdir -p %s" % project_name)
    run("cd /usr/local/%s; mkdir -p log config data release" % project_name)
    run("cd /usr/local/%s/release; svn co %s" % (project_name, project_uri_testing))
    run("cd /usr/local/%s; ln -fs release/%s current" % (project_name, project_uri_testing.split('/')[-1]))
    run("cd /usr/local/%s/current; pip install -r requirements.txt; python setup.py install" % project_name)


def deploy_development():
    run("cd /usr/local; mkdir -p %s" % project_name)
    run("cd /usr/local/%s; mkdir -p log config data release" % project_name)
    run("cd /usr/local/%s/release; svn co %s" % (project_name, project_uri_production))
    run("cd /usr/local/%s; ln -fs release/%s current" % (project_name, project_uri_production.split('/')[-1]))
    run("cd /usr/local/%s/current; pip install -r requirements.txt; python setup.py install" % project_name)