# 核心功能: 是将模型转化Json数据

from rest_framework import serializers
from home.models import TFilm, TCateLog


class TFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TFilm
        fields = '__all__'


# 一对多转换Json数据
class TCateLogSerializer(serializers.ModelSerializer):
    # cate_log_id = models.ForeignKey('TCateLog', on_delete=models.DO_NOTHING, related_name='films')
    films = TFilmSerializer(many=True, read_only=True)  #
    # 如果要用别名films 则需在模型字段内加上 related_name='films' 否则只能模型类名小写_set :tfilm_set

    class Meta:
        model = TCateLog
        fields = '__all__'
