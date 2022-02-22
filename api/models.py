from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date, datetime

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
from django.contrib.auth.models import BaseUserManager, AbstractUser

# from shortsighted import ShortUUIDField # 使用shortuuid作为User表的主键，使数据更加的安全
from django.utils import timezone

import api.models


class UserManager(BaseUserManager):  # 自定义Manager管理器
    def _create_user(self, phone, password, **kwargs):
        if not phone:
            raise ValueError("请传入id card！")
        if not password:
            raise ValueError("请传入电话")
        user = self.model(phone=phone, password=password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, phone, password, **kwargs):  # 创建普通用户
        kwargs['is_superuser'] = False
        return self._create_user(phone, password, **kwargs)

    def create_superuser(self, phone, password, **kwargs):  # 创建超级用户
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(phone, password, **kwargs)


class User(AbstractUser):  # 自定义User
    GENDER_TYPE = (
        ("1", "男"),
        ("2", "女")
    )
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, verbose_name="用户名")
    nickname = models.CharField(max_length=13, verbose_name="昵称", null=True, blank=True)
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True)
    sex = models.CharField(max_length=10, default='女', verbose_name='性别')
    gender = models.CharField(max_length=2, choices=GENDER_TYPE, verbose_name="性别", null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    email = models.EmailField(verbose_name="邮箱")
    # picture = models.ImageField(upload_to="Store/user_picture",verbose_name="用户头像",null=True,blank=True)
    home_address = models.CharField(max_length=100, null=True, blank=True, verbose_name="地址")
    # region = models.ForeignKey(Region, verbose_name="region", null=True, on_delete=models.SET_NULL)
    card_id = models.CharField(max_length=30, verbose_name="身份证", null=True)
    is_active = models.BooleanField(default=True, verbose_name="激活状态")
    is_staff = models.BooleanField(default=True, verbose_name="是否是员工")
    # date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'  # 使用authenticate验证时使用的验证字段，可以换成其他字段，但验证字段必须是唯一的，即设置了unique=True
    REQUIRED_FIELDS = ['email']  # 创建用户时必须填写的字段，除了该列表里的字段还包括password字段以及USERNAME_FIELD中的字段
    EMAIL_FIELD = 'email'  # 发送邮件时使用的字段

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name="投放区域")
    code = models.CharField(max_length=10, verbose_name="邀请码")
    start_time = models.DateField(default=timezone.now, verbose_name="开始时间")
    end_time = models.DateField(default=timezone.now, verbose_name="结束时间")
    credit = models.IntegerField(default=0, verbose_name="预算案例")
    left_credit = models.IntegerField(default=0, verbose_name='剩余份额')
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="发送人")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "投放区域"
        verbose_name_plural = "投放区域"


class CheckProject(models.Model):
    name = models.CharField(max_length=20, verbose_name="活动名称")
    department_name = models.TextField(verbose_name="负责科室")
    department_position = models.TextField(verbose_name="科室位置")
    check_agent = models.TextField(verbose_name="科目")
    check_item = models.TextField(null=True, verbose_name="检查范围")
    announcement = models.TextField(verbose_name="通知")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    contact = models.ForeignKey(User, verbose_name="联系人", on_delete=models.CASCADE)
    credit = models.IntegerField(verbose_name="预算案例", null=True)
    left_credit = models.IntegerField(verbose_name='剩余份额', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "检查计划"
        verbose_name_plural = "检查计划"


CheckReportChoices = (
    ("Finished", "报告已完成"),
    ("Unfinished", "报告未填写")
)


class CheckReport(models.Model):
    # checkitem = models.ForeignKey(CheckItem, null=True, related_name="check_user", on_delete=models.CASCADE,
    #                          verbose_name="检查用户")
    name = models.CharField(max_length=50, verbose_name="检查报告名称")
    status = models.CharField(max_length=50, choices=CheckReportChoices, default="Unfinished", verbose_name='状态')
    main = models.TextField(null=True, blank=True, verbose_name="主诉")
    disease_history = models.TextField(null=True, blank=True, verbose_name="病史")
    drug_history = models.TextField(null=True, blank=True, verbose_name="药物过敏史")
    body_check = models.TextField(null=True, blank=True, verbose_name="体格检查")
    diagnose = models.TextField(null=True, blank=True, verbose_name="初步诊断")
    treatment = models.TextField(null=True, blank=True, verbose_name="处置")

    def __str__(self):
        # return self.checkitem.first().user.username
        return self.name

    class Meta:
        verbose_name = "检查报告"
        verbose_name_plural = "检查报告"


Text_Choice = (
    ("Finished", "已完成体检报告",),
    ("Unfinished", "未完成体检报告"),
    ("Waiting", "等待检查",)
)


class CheckItem(models.Model):
    user = models.ForeignKey(User, null=True, related_name="check_user", on_delete=models.CASCADE,
                             verbose_name="检查用户")
    check_project = models.ForeignKey(CheckProject, null=True, on_delete=models.CASCADE,
                                      verbose_name="检查项目")
    region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)
    check_date = models.DateTimeField(null=True, verbose_name="预计开始时间")
    check_am_pm = models.CharField(max_length=20, default="am")
    check_number = models.IntegerField(verbose_name="检查编号")
    doctor = models.ForeignKey(User, null=True, related_name="check_doctor", on_delete=models.CASCADE,
                               verbose_name="检查医生")
    status = models.CharField(max_length=100, choices=Text_Choice, default="Waiting", verbose_name='状态')
    check_report = models.OneToOneField(CheckReport, related_name="checkitem", null=True, blank=True,
                                        on_delete=models.CASCADE,
                                        verbose_name="检查报告")

    def __str__(self):
        return str(self.check_number)

    class Meta:
        verbose_name = "门诊预约单"
        verbose_name_plural = "门诊预约单"


class TimeSheet(models.Model):
    check_project = models.ForeignKey(CheckProject, on_delete=models.CASCADE,
                                      verbose_name="门诊预约单")
    time = models.DateField(verbose_name="日期")
    is_holiday = models.BooleanField(default=False, verbose_name="是否是节假日")
    am = models.PositiveIntegerField(default=20, verbose_name="上午访问人数")
    pm = models.PositiveIntegerField(default=20, verbose_name="下午访问人数")

    def __str__(self):
        return str(self.time)

    class Meta:
        ordering = ['time', 'am']
        verbose_name = "时间表"
        verbose_name_plural = "时间表"


class Disease(models.Model):
    group = models.TextField()
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '疾病'
        verbose_name_plural = '疾病'


