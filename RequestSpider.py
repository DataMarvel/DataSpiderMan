# -*- coding: UTF-8 -*-
"""
Created on 2018年11月15日
@author: Leo
@file: RequestSpider
"""
# Python第三方库
import requests

# 项目内部库
from DataSpiderMan.spider.BaseSpider import BaseSpider


class RequestSpider(BaseSpider):

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
        :return: request.Response
        """
        if url == "":
            url = self._url
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
