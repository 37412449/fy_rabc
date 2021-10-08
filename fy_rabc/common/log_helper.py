# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from loguru import logger
import os
import threading
import sys
import json

Base_Root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(Base_Root)


class log_helper(object):
    _instance_lock = threading.Lock()
    myLogger = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(log_helper, "_instance"):
            with log_helper._instance_lock:
                if not hasattr(log_helper, "_instance"):
                    log_helper._instance = object.__new__(cls)
                    cls.createLogger()
        return log_helper._instance

    @property
    def logger(self):
        if self.myLogger is None:
            self.createLogger()
        return self.myLogger

    @classmethod
    def createLogger(cls):
        cls.myLogger = logger

        # 错误日志
        cls.myLogger.add(
            os.path.join(Base_Root, "log/err/{time:YYYYMMDD}.log"),
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            filter=lambda x: True if x["level"].name == "ERROR" else False,
            rotation="00:00", retention=7, level='ERROR', encoding='utf-8'
        )
        # 消息日志
        cls.myLogger.add(
            os.path.join(Base_Root, "log/info/{time:YYYYMMDD}.log"),
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            filter=lambda x: True if x["level"].name == "INFO" else False,
            rotation="00:00", retention=7, level='INFO', encoding='utf-8',
        )
        '''
        # Default日志
        cls.myLogger.add(
            os.path.join(Base_Root, "log/debug/{time:YYYYMMDD}.log"),
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            rotation="00:00", retention=7, level='DEBUG', encoding='utf-8'
        )
        '''

    @classmethod
    def infoMsg(cls, request):
        if request.method == 'POST':
            try:
                # 参数
                infoPar = '['
                if request.body:
                    reData = str(request.body, encoding="utf-8")
                    jsData = json.loads(reData)
                    if jsData:
                        for key in jsData.keys():
                            infoPar = infoPar + key + ":" + str(jsData[key]) + ","
                infoPar = infoPar.rstrip(',') + "]"

                # 路径
                infoPath = ''
                if request.path:
                    infoPath = request.path

                # 用户
                infoUser = ''
                if request.user:
                    infoUser = request.user.username

                # 写日志
                cls.myLogger.info("用户:" + infoUser + ";操作:" + infoPath + ";参数:" + infoPar)
            except Exception as e:
                print(str(e))
