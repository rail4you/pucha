from urllib.parse import urlencode

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import User
from django.urls import reverse
from django.utils.html import format_html

from api.models import User, CheckProject, CheckReport, CheckItem, Region
from api.models import TimeSheet


@admin.register(CheckProject)
class CheckProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time", "credit")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time", "credit")

@admin.register(CheckItem)
class CheckItemAdmin(admin.ModelAdmin):
    list_display = ("user", "check_number", "user_sex", "user_age", "check_date", "status", "check_report_link")

    def user_sex(self, obj):
        user = obj.user.sex
        return user
    user_sex.short_description = '性别'

    def user_age(self, obj):
        return obj.user.age
    user_age.short_description = '年龄'

    def check_report_link(self, obj):
        check_report = obj.check_report
        if check_report is None:
           url = (reverse("admin:api_checkreport_add"))
           return format_html('<a href="{}">写检查报告</a>', url)
        else:
            url = (
                    reverse("admin:api_checkreport_change", args=[check_report.id])
                    # + f"/{check_report.id}/change/"
                    # + urlencode({"pk": f"{check_report.id}"})
            )
            print(url)
            return format_html('<a href="{}">编辑检查报告</a>', url)


    list_filter = ("status",)

admin.site.register(User)
admin.site.register(TimeSheet)
# admin.site.register(CheckProject)
admin.site.register(CheckReport)
# admin.site.register(CheckItem)
# Register your models here.
