# -*- coding: UTF-8 -*-
"""
Created on 2018年11月15日
@author: Leo
@file: UrllibSpider
"""
import socket
import urllib.parse as up
import urllib.request as ur

# 项目内部库
from DataSpiderMan.spider.BaseSpider import BaseSpider
from DataVision.LoggerHandler.logger import VisionLogger

# 日志路径
LOGGER_PATH = '../../DataVision/LoggerConfig/logger_config.yaml'


class UrllibSpider(BaseSpider):

    def get(self,
            url: str = ""):
        pass
