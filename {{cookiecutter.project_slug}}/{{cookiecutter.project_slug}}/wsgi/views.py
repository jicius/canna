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

import time

from pif import get_public_ip
from flask.views import MethodView
from flask import (render_template, jsonify)
from flask_mail import Message

from {{ cookiecutter.project_name }} import (app, mail)


class WelcomeCanna(MethodView):
    """ 欢迎页
    
    """
    def get(self):
        return render_template('welcome.html')


class MailAlter(MethodView):
    """ 邮件监控

    关键服务邮件监控通知
    """
    def get(self):
        host = get_public_ip()
        msg = Message(
            subject="%s - Daily Summary - %s" % ({{ cookiecutter.project_name}}, time.ctime()),
            sender=("Canna Notifier", "2644148694@qq.com"),  # sender是一个二元组, 分别为姓名和邮件地址
            recipients=[
                {{ cookiecutter.mail_receiver }}
            ]
        )
        items = []
        msg.html = render_template('email.html', items=items, title="canna.notifier", host=host)
        try:
            mail.send(msg)
        except Exception as e:
            return jsonify(dict(Code=-1, State=e))
        return jsonify(dict(Code=0, State="Ok"))


# 注册路由
app.add_url_rule("/", view_func=WelcomeCanna.as_view('welcome'))
app.add_url_rule("/send_mail", view_func=MailAlter.as_view('send_mail'))