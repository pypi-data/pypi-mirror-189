# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 10:32

import os
from se_imports import se_register_module
__is_ready__ = False
project_data_dir =  os.path.abspath(os.path.join(os.path.dirname(__file__),'.__data__.pys'))
if not __is_ready__ and os.path.exists(project_data_dir):
    __is_ready__ = True
    root_dir = os.path.abspath(os.path.dirname(__file__))
    se_register_module(root_dir=root_dir)
