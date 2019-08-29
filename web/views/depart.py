#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import StarkHandler
from .base import PermissionHandler


class DepartmentHandler(PermissionHandler,StarkHandler,):
    list_display = ['title',StarkHandler.display_edit_del ]
