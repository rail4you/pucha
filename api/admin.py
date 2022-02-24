from django.contrib import admin
# from .models import User
from django.urls import reverse
from django.utils.html import format_html
from django_reverse_admin import ReverseModelAdmin

from api.models import TimeSheet
from api.models import User, CheckProject, CheckReport, CheckItem, Region, Disease


@admin.register(CheckProject)
class CheckProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time", "credit")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time", "credit")


# class CheckItemInline(admin.StackedInline):
#     model = CheckItem
#     fk_name = "user"

# class UserInline(admin.StackedInline):
#     model = User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
# list_display = ('username', 'phone')
# inlines = [CheckItemInline]

#
#
# classs CheckItemForm(forms.Mo)


# @admin.register(CheckItem)
class CheckItemAdmin(ReverseModelAdmin):
    list_display = ("user", "check_number", "user_sex", "user_age", "check_date", "status", "check_report_link")
    # list_display_links = None
    readonly_fields = ('user', 'check_report')
    fields = ('user',)
    # inlines = (UserInline, )
    inline_type = 'stacked'
    inline_reverse = [('user', {'fields': ['username', 'age', 'phone']}),
                      ('check_project', {'fields': ['name', 'left_credit']}),
                      'check_report',
                      ]

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


@admin.register(CheckReport)
class CheckReportAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    # inlines = (CheckItemInline, )


admin.site.register(User)
admin.site.register(TimeSheet)
# admin.site.register(CheckProject)
# admin.site.register(CheckReport)
admin.site.register(CheckItem)
admin.site.register(Disease)
# Register your models here.
