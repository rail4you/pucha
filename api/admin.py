from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import User
from api.models import User, CheckProject
from api.models import TimeSheet

admin.site.register(User, UserAdmin)
admin.site.register(TimeSheet)
admin.site.register(CheckProject)
# Register your models here.
