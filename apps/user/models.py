from django.db import models
from django.contrib.auth.models import AbstractUser
from db.bash_model import BaseModel
from tinymce.models import HTMLField
# Create your models here.


class User(AbstractUser, BaseModel):
    '''用户模型类'''

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    '''地址模型类'''
    user = models.ForeignKey('User', verbose_name='所属账户',on_delete=models.CASCADE,)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

class MceTest(models.Model):
    status_choices = (
        (0, 'good'),
        (1, 'bad')
    )

    status = models.SmallIntegerField(default=1, choices=status_choices)
    detail = HTMLField(verbose_name='测试富文本')

    class Meta:
        db_table = 'df_test_mcd'
        verbose_name = 'test_mce'
        verbose_name_plural = verbose_name