from django.shortcuts import render
from rest_framework.views import APIView

from apps.home.models import TFilm, TCateLog

# rest 的核心功能 模型转化为json
from home.home_serializers import TFilmSerializer, TCateLogSerializer
# 的数据结构化封装程序
from common.result import ResultsResponse


def index(request):
    return render(request, 'index.html')


def details(request):
    return render(request, 'details.html')


class TFilmView(APIView):
    def get(self, request):
        try:
            films = TFilm.objects.all()
            serializer = TFilmSerializer(films, many=True)
            return ResultsResponse.success_to_response(data=serializer.data)
        except Exception as e:
            print(e)
            return ResultsResponse.error_to_response()


class TCateView(APIView):
    def get(self, request):
        try:
            cate_list = TCateLog.objects.all()
            ser = TCateLogSerializer(cate_list, many=True)
            return ResultsResponse.success_to_response(data=ser.data)
        except Exception as e:
            print(e)
            return ResultsResponse.error_to_response()
