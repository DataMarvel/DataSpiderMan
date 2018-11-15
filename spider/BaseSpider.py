# -*- coding: UTF-8 -*-
"""
Created on 2018年11月15日
@author: Leo
@file: BaseSpider
"""

# 项目内部库
from DataVision.LoggerHandler.logger import VisionLogger

# 日志路径
LOGGER_PATH = '../../DataVision/LoggerConfig/logger_config.yaml'


class BaseSpider(object):

    def __init__(self,
                 spider_url: str = "",
                 headers: dict = None,
                 timeout: int = 30,
                 retry_num: int = 3):
        """
        UrllibSpider
        :param spider_url: 爬虫URL
        :param headers: 爬虫请求头
        :param timeout: 超时秒数
        :param retry_num: 重试次数
        """

        # 日志
        self._logger = VisionLogger(LOGGER_PATH)

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
