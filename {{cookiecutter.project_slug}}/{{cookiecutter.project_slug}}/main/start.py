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

import sys


class DoFuncs(object):
    """ 主函数
    
    项目核心主流程
    """
    def __init__(self):
        pass

    @classmethod
    def func_1(cls):
        pass

    @classmethod
    def func_2(cls):
        pass


# 调用函数说明
# @func: func_1, func 1
# @func: func_2, func 2
def do_func(func_name):
    if func_name == "func_1":
        DoFuncs.func_1()
    elif func_name == "func_2":
        DoFuncs.func_2()
    else:
        raise Exception("Error, func invoke failed.")


if __name__ == '__main__':
    func_name = sys.argv[1]
    do_func(func_name=func_name)