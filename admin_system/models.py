from django.db import models
from datetime import datetime


class Categories(models.Model):
    icon_choice = (
        ('最多喜欢的用户', 'fa-user'),
        ('最多收藏', 'fa-star-o'),
        ('最多点赞', 'fa-thumbs-o-up'),
        ('最多亮灯/赞助', 'fa-lightbulb-o'),
        ('最多转发', 'fa-bullhorn')
    )

    id = models.AutoField(verbose_name='类别编号', primary_key=True)
    parent_id = models.IntegerField(verbose_name='parent_id')
    order = models.IntegerField(verbose_name='顺序')
    title = models.CharField(verbose_name='分类标题', max_length=128)
    icon = models.CharField(verbose_name='图标', max_length=128, choices=icon_choice)
    created_at = models.DateTimeField(verbose_name='创建时间')
    updated_at = models.DateTimeField(verbose_name='更新时间')

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        db_table = "categories"


class Sites(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    # category_id = models.IntegerField(verbose_name='类别编号')
    category = \
        models.ForeignKey(
            verbose_name='类别编号',
            to=Categories,
            on_delete=models.CASCADE,
            null=True,
        )

    title = models.CharField(verbose_name='网站标题', max_length=128)
    thumb = models.CharField(default='images/37a9bff7f4d756e7b227ef295aa5ff82.png', verbose_name='网站logo', max_length=128)
    describe = models.CharField(verbose_name='网站描述', max_length=128)
    url = models.CharField(verbose_name='网站链接', max_length=128)
    created_at = models.DateTimeField(verbose_name='创建时间', default=datetime.now())
    updated_at = models.DateTimeField(verbose_name='更新时间', default=datetime.now())

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        db_table = "sites"

