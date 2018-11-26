from django.db import models


class TCateLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_cate_log'


class TDecade(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_decade'


class TFilm(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cate_log_name = models.CharField(max_length=255)
    cate_log = models.ForeignKey('TCateLog', on_delete=models.DO_NOTHING, related_name='films')
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc = models.ForeignKey('TLoc', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.ForeignKey('TDecade', on_delete=models.DO_NOTHING, db_column='on_decade', blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class = models.ForeignKey('TSubclass', on_delete=models.DO_NOTHING, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('TType', on_delete=models.DO_NOTHING, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_film'


class TLevel(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_level'


class TLoc(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_loc'


class TRaty(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    en_time = models.CharField(max_length=255, blank=True, null=True)
    film_id = models.ForeignKey('TFilm', on_delete=models.DO_NOTHING, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 't_raty'


class TRes(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    episodes = models.IntegerField()
    is_use = models.IntegerField()
    link = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    film_id = models.ForeignKey('TFilm', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_res'


class TSubclass(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    catelog_id = models.ForeignKey('TCateLog', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_subclass'


class TType(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    subclass_id = models.ForeignKey('TSubclass', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_type'


class TUser(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    is_vip = models.BigIntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    passwd = models.CharField(max_length=255, blank=True, null=True)
    is_manager = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_user'


class TVipcode(models.Model):
    id = models.CharField(primary_key=True, max_length=225)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 't_vipcode'
