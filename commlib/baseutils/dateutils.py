#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2016-04-11

@author: Devin
"""
import datetime
from dateutil.relativedelta import relativedelta


def timetstr(t_date=datetime.datetime.now(), format="%Y%m%d%H%M%S"):
    return t_date.strftime(format)


def timefstr(s_date, format="%Y%m%d%H%M%S"):
    t_date = datetime.datetime.strptime(s_date, format)
    return t_date


def add_month(s_date, add_months=0):
    return s_date + relativedelta(months=add_months)
