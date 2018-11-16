# -*- coding: UTF-8 -*-
"""
Created on 2018年11月15日
@author: Leo
@file: UrllibSpider
"""
import json
import socket
import urllib.parse as up
import urllib.request as ur

# 项目内部库
from DataSpiderMan.spider.BaseSpider import BaseSpider


class UrllibSpider(BaseSpider):

    def get(self,
            url: str = "",
            data: dict = None):
        """
        发送GET请求
        :param url: 请求url
        :param data: 数据 dict
        :return: http.client.HTTPResponse
        """
        # 超时时间
        socket.setdefaulttimeout(self.timeout)
        # 判断URL
        if url == "":
            url = self._url
        # GET参数
        if data is not None:
            params = "?"
            for key in data:
                params = params + key + "=" + data[key] + "&"
            url += params
        # 输出URL
        self._logger.vision_logger(level='INFO', log_msg=url)
        # 重试机制
        for i in range(self.retry_num):
            try:
                request = ur.Request(url=url, headers=self.headers)
                response = ur.urlopen(request)
                print(response)
                return response
            except BaseException as err:
                self._logger.vision_logger(level='ERROR', log_msg=str(err))
                if i == self.retry_num - 1:
                    self._logger.vision_logger(level='ERROR', log_msg="超过重试次数!")

    def post(self,
             url: str = "",
             data: dict = None,
             json_data: dict = None):
        """
        发送POST请求
        :param url: 请求URL
        :param data: data参数
        :param json_data: json参数
        :return: http.client.HTTPResponse
        """
        # 超时时间
        socket.setdefaulttimeout(self.timeout)
        # 判断URL
        if url == "":
            url = self._url
        # data或者json处理
        if data is not None:
            data = up.urlencode(data).encode('UTF-8')
        else:
            if json_data is not None:
                data = json.dumps(json_data).encode('UTF-8')
            else:
                raise ValueError("data和json_data参数缺失")
        # 重试机制
        for i in range(self.retry_num):
            try:
                request = ur.Request(url=url, headers=self.headers, data=data)
                response = ur.urlopen(request)
                return response
            except BaseException as err:
                self._logger.vision_logger(level='ERROR', log_msg=str(err))
                if i == self.retry_num - 1:
                    self._logger.vision_logger(level='ERROR', log_msg="超过重试次数!")
