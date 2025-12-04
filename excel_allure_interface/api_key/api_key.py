
import json

import allure
import pymysql
import pytest
from jsonpath import jsonpath
import requests

@allure.feature('封装ak')
class ApiKey:
    @allure.step('发送post请求')  # 能够自动识别参数，并打印出来
    def post(self, url, params=None, **kwargs):
        return requests.post(url=url, params=params, **kwargs)

    @allure.step('发送get请求')
    def get(self, url, data=None, json=None, **kwargs):
        return requests.get(url, data=data, json=json, **kwargs)

    @allure.step('抽取数据')
    def get_text(self, res, express):
        resp = json.loads(res)
        tmp = jsonpath(resp, express)
        return tmp[0]

    @allure.step('数据库校验')
    def sql_check(self):
        # 1、数据库链接
        conn = pymysql.connect(
            host='172.22.5.31',
            port=3306,
            user='xpark',
            password='Flyitem@2016',
            database='tsyg',
            charset='utf8'
        )
        # 2、创建游标
        cur = conn.cursor()
        # 3、执行sql
        cur.execute("select record_bonus_level from sxo_user where uuid = '100000000'")
        # 查询100000000的计奖级别
        # 4、获取查询结果
        # res = cur.fetchmany(n)
        results = cur.fetchmany()[0]
        for row in results:
            # print(row)
            pass
        # 5、关闭
        cur.close()
        conn.close()
        return results

    @allure.step('加密')
    def code(self):
        print("我是校验码")

    @allure.step('签名')
    def sign(self):
        pass

ak = ApiKey()

if __name__ == '__main__':

    print(ak.sql_check())

