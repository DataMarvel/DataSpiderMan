# -*- coding: UTF-8 -*-
"""
Created on 2018年11月15日
@author: Leo
@file: RequestSpider
"""
# Python第三方库
import requests

# 项目内部库
from DataVision.LoggerHandler.logger import VisionLogger

# 日志路径
LOGGER_PATH = '../../DataVision/LoggerConfig/logger_config.yaml'


class RequestSpider(object):

    def __init__(self,
                 spider_url: str = "",
                 headers: dict = None,
                 timeout: int = 30,
                 retry_num: int = 3):
        """
        RequestSpider
        :param spider_url: 爬虫URL
        :param headers: 爬虫请求头
        :param timeout: 超时秒数
        :param retry_num: 重试次数
        """
        # 日志
        self._logger = VisionLogger(LOGGER_PATH)

        # session对象
        self.session = requests.session()

        # 请求URL
        self._url = spider_url

        # 请求头
        self.headers = headers
        if self.headers is None:
            self.headers = {"User-Agent": "DataSpiderMan"}

        # 默认60s
        self.timeout = timeout

        # http连接异常的场合，重新连接的次数，默认为3，可以动态设定
        self.retry_num = retry_num

    def get(self,
            url: str = "",
            params=None,
            **kwargs):
        """
        发送GET请求
        :param url: 请求url
        :param params: 参数
        :param kwargs: 其他参数(request有的)
        :return: request.Response
        """
        if url == "":
            url = self._url
        else:
            raise ValueError("请求缺少URL参数")
        # 加入重试机制
        for i in range(self.retry_num):
            try:
                kwargs.setdefault('allow_redirects', True)
                kwargs.setdefault('timeout', self.timeout)
                kwargs.setdefault('headers', self.headers)
                response = requests.get(url=url, params=params, **kwargs)
                return response
            except BaseException as err:
                self._logger.vision_logger(level='ERROR', log_msg=str(err))
                if i == self.retry_num - 1:
                    self._logger.vision_logger(level='ERROR', log_msg="超过重试次数!")

    def post(self,
             url: str = "",
             data=None,
             json=None,
             **kwargs):
        """
        发送POST请求
        :param url: 请求URL
        :param data: data参数
        :param json: json参数
        :param kwargs: 其他参数(request有的)
        :return: request.Respnse
        """
        if url == "":
            url = self._url
        else:
            raise ValueError("请求缺少URL参数")
            # 加入重试机制
        for i in range(self.retry_num):
            try:
                kwargs.setdefault('timeout', self.timeout)
                kwargs.setdefault('headers', self.headers)
                response = requests.post(url=url, data=data, json=json, **kwargs)
                return response
            except BaseException as err:
                self._logger.vision_logger(level='ERROR', log_msg=str(err))
                if i == self.retry_num - 1:
                    self._logger.vision_logger(level='ERROR', log_msg="超过重试次数!")


# if __name__ == '__main__':
    # r = RequestSpider(spider_url='http://172.18.172.199/client-web/clientLogin/loginUser', timeout=2)
    # payload = "userCode=1&password=1&codeInput=1&phoneNumber=1"
    # res = r.post(data=payload)
    # print(res)
    # print(res.request.headers)
