from django.http import JsonResponse
from rest_framework import status

STATUS_LOGIN_CODE = 200
MSG_SUCCESS_STR = 'ok'

'''
HTTP_200_OK:是rest自带的状态码
status=status.HTTP_200_OK   HTTP_200_OK:是rest自带的状态码

定义常量方便修改
STATUS_LOGIN_CODE = 1
MSG_SUCCESS_STR = 'ok'
'''


class ResultsResponse:
    @staticmethod
    def success_to_response(data, status=STATUS_LOGIN_CODE, msg=MSG_SUCCESS_STR):
        res = {'status': status, 'msg': msg, 'data': data}
        return JsonResponse(res)

    @staticmethod
    def error_to_response(status=404, msg='error'):
        res = {'status': status, 'msg': msg}
        return JsonResponse(res)
