from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


# class User(AbstractUser):
#     username = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     email = models.EmailField('email', unique=True)
#     native_name = models.CharField(max_length=5)
#     phone_no = models.CharField(max_length=10)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#
#     def __str__(self):
#         return "{}".format(self.email)
from django.contrib.auth.models import BaseUserManager,AbstractUser
# from shortuuidfield import ShortUUIDField # 使用shortuuid作为User表的主键，使数据更加的安全

class UserManager(BaseUserManager): #自定义Manager管理器
    def _create_user(self,username,id_card,phone,**kwargs):
        if not username:
            raise ValueError("请传入用户名！")
        if not id_card:
            raise ValueError("请传入id card！")
        if not phone:
            raise ValueError("请传入电话")
        user = self.model(username=username,id_card=id_card, phone=phone,**kwargs)
        # user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,email,**kwargs): # 创建普通用户
        kwargs['is_superuser'] = False
        return self._create_user(username,password,email,**kwargs)

    def create_superuser(self,username,password,email,**kwargs): # 创建超级用户
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,email,**kwargs)

class User(AbstractUser): # 自定义User
    GENDER_TYPE = (
        ("1","男"),
        ("2","女")
    )
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15,verbose_name="用户名")
    nickname = models.CharField(max_length=13,verbose_name="昵称",null=True,blank=True)
    age = models.IntegerField(verbose_name="年龄",null=True,blank=True)
    gender = models.CharField(max_length=2,choices=GENDER_TYPE,verbose_name="性别",null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,verbose_name="手机号码")
    email = models.EmailField(verbose_name="邮箱")
    # picture = models.ImageField(upload_to="Store/user_picture",verbose_name="用户头像",null=True,blank=True)
    home_address = models.CharField(max_length=100,null=True,blank=True,verbose_name="地址")
    card_id = models.CharField(max_length=30,verbose_name="身份证", unique=True)
    is_active = models.BooleanField(default=True,verbose_name="激活状态")
    is_staff = models.BooleanField(default=True,verbose_name="是否是员工")
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'card_id' # 使用authenticate验证时使用的验证字段，可以换成其他字段，但验证字段必须是唯一的，即设置了unique=True
    REQUIRED_FIELDS = ['email'] # 创建用户时必须填写的字段，除了该列表里的字段还包括password字段以及USERNAME_FIELD中的字段
    EMAIL_FIELD = 'email' # 发送邮件时使用的字段

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name