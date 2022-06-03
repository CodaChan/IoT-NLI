# Copyright 2021 plainfebruary
# Completed on September 9, 2021

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkiot.request.v20180120.QueryDeviceGroupListRequest import QueryDeviceGroupListRequest
from aliyunsdkiot.request.v20180120.QueryDeviceListByDeviceGroupRequest import QueryDeviceListByDeviceGroupRequest
from aliyunsdkiot.request.v20180120.QueryThingModelRequest import QueryThingModelRequest


class LDPRT:
    @staticmethod
    def tree():
        client = AcsClient('LTAI5tRzYTBkP3FQCTHR1zkr', 'yuw7AzH1lMWZhpN7otjcTspF1vAkV7', 'cn-shanghai')
        tree = []

        request_0 = QueryDeviceGroupListRequest()
        request_0.set_accept_format('json')
        response_0 = client.do_action_with_exception(request_0)
        result_str_0 = str(response_0, encoding='utf-8')
        result_0 = json.loads(result_str_0)
        for i in range(result_0['Total']):
            group_temp = {}
            group_temp['GroupId'] = result_0['Data']['GroupInfo'][i]['GroupId']
            group_temp['GroupName'] = result_0['Data']['GroupInfo'][i]['GroupName']
            tree.append(group_temp)
        request_1 = QueryDeviceListByDeviceGroupRequest()
        request_1.set_accept_format('json')

        for i in range(len(tree)):
            request_1.set_GroupId(tree[i]['GroupId'])
            response_1 = client.do_action_with_exception(request_1)
            result_str_1 = str(response_1, encoding='utf-8')
            result_1 = json.loads(result_str_1)
            tree[i]['Device'] = []
            for j in range(len(result_1['Data']['SimpleDeviceInfo'])):
                tree[i]['Device'].append(result_1['Data']['SimpleDeviceInfo'][j])

        return tree

    @staticmethod
    def final(ProductKey):
        client = AcsClient('LTAI5tRzYTBkP3FQCTHR1zkr', 'yuw7AzH1lMWZhpN7otjcTspF1vAkV7', 'cn-shanghai')
        request = QueryThingModelRequest()
        request.set_accept_format('json')
        request.set_ProductKey(ProductKey)
        response = client.do_action_with_exception(request)
        result_str_2 = (str(response, encoding='utf-8'))
        result_2 = json.loads(result_str_2)
        result_2 = json.loads(result_2['Data']['ThingModelJson'])
        return result_2['properties']
print(LDPRT.tree())
print(LDPRT.final(LDPRT.tree()[0]['Device'][1]['ProductKey']))
