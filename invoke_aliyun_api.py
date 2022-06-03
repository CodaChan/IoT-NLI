# Copyright 2021 plainfebruary
# Completed on September 11, 2021

import time
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkiot.request.v20180120.SetDevicePropertyRequest import SetDevicePropertyRequest
from aliyunsdkiot.request.v20180120.QueryDevicePropertyDataRequest import QueryDevicePropertyDataRequest
from aliyunsdkiot.request.v20180120.DisableThingRequest import DisableThingRequest


class Practice:
    def control(ProductKey, DeviceName, items):
        client = AcsClient('LTAI5tRzYTBkP3FQCTHR1zkr', 'yuw7AzH1lMWZhpN7otjcTspF1vAkV7', 'cn-shanghai')

        request = SetDevicePropertyRequest()
        request.set_accept_format('json')
        request.set_Items(items)
        request.set_DeviceName(DeviceName)
        request.set_ProductKey(ProductKey)
        response = client.do_action_with_exception(request)

        print(response)

    def query(ProductKey, DeviceName, identifier):
        client = AcsClient('LTAI5tRzYTBkP3FQCTHR1zkr', 'yuw7AzH1lMWZhpN7otjcTspF1vAkV7', 'cn-shanghai')

        request = QueryDevicePropertyDataRequest()
        request.set_accept_format('json')
        request.set_Asc("1")
        request.set_PageSize("10")
        request.set_Identifier(identifier)
        request.set_StartTime(int(round(1000 * (time.time()))) - 5000)
        request.set_EndTime(20000 + int(round(1000 * (time.time()))))
        request.set_IotId("")
        request.set_ProductKey(ProductKey)
        request.set_DeviceName(DeviceName)

        response = client.do_action_with_exception(request)
        result_str = str(response, encoding='utf-8')
        result = json.loads(result_str)

        print(result)
