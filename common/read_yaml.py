#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-08-29 13:47
# @Author  : TOM
# @File    : read_yaml.py
# @Software: PyCharm

import json
import os
import yaml


class ReadYaml:
    # 获取yaml文件路径
    yaml_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'conf',
        'setting.yaml',
    )

    def __init__(self, key):
        self.key = key

    def get_data(self):
        with open(self.yaml_path, 'r', encoding='utf8') as f:
            data_yaml = yaml.load(f, Loader=yaml.FullLoader)[self.key]
        # 返回单据类型下的测试数据，并进行编码处理，避免中文乱码
        return json.dumps(data_yaml, ensure_ascii=False)


if __name__ == '__main__':
    r_uri = ReadYaml(key='filename').get_data()
    r_data = ReadYaml(key='正式').get_data()
    print(r_data)
    print(r_uri)
