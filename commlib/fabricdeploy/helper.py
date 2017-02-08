#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: helper.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-06 14:09:39 (CST)
# Last Update:星期二 2016-12-6 14:18:58 (CST)
#          By:
# Description:
# **************************************************************************
import os

from fabric.contrib import files
from fabric.decorators import with_settings
from fabric.operations import run
from fabric.state import env
from fabric.utils import abort, error


def check(pro):
    if hasattr(env, pro) and getattr(env, pro):
        return True
    return False


def empty_folder(path):
    if files.exists(path):
        return run("ls -l %s | wc -l" % path) <= str(1)
    return True


@with_settings(warn_only=True)
def overwrite_template(keep_trailing_newline=False, **config):
    '''
    前端代码替换
    :param keep_trailing_newline:
    :param config:
    :return:
    '''
    template_dir = config.get("template_dir", os.getcwd())
    filename = config.get("filename")
    context = config.get("context", {})
    destination = config.get("destination")
    from jinja2 import Environment, FileSystemLoader
    jenv = Environment(loader=FileSystemLoader(template_dir),
                       keep_trailing_newline=keep_trailing_newline)
    roles = env.effective_roles
    if len(roles) > 1:
        abort("指定了多个环境role[%s],模版无法匹配" % str(roles))
    elif len(roles) == 0:
        error("没有指定环境role")
    tmp_context = context.get(roles[0], {})
    text = jenv.get_template(filename).render(**tmp_context or {})
    with open(destination, 'w') as f:
        f.write(text)
        f.flush()
