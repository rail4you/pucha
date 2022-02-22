import json
from datetime import datetime

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# obtain_auth_token = ObtainAuthToken.as_view()
from api.models import CheckItem, CheckProject, Region, User, Disease
from api.serializers import DiseaseSerializer, CheckReportSerializer
from api.utils import add_time_interval, get_paginated_list


class ObtainAuthToken(APIView):
    permission_classes = ()  # <-- And here

    def post(self, request, *args, **kwargs):
        dic = request.data
        user, _ = User.objects.get_or_create(username=dic["username"], phone=dic["phone"], card_id=dic["card_id"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(phone=phone, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response("login failed")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)  # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CheckCodeView(APIView):
    permission_classes = ()

    def get(self, request):
        code = request.GET.get("code")
        region = Region.objects.filter(code=code).first()
        if region is None:
            return Response("no region")
        else:
            return Response(region.id)


class RegionDetailView(APIView):
    permission_classes = ()

    def get(self, request, pk):
        region = get_object_or_404(Region, pk=pk)
        dic = {"name": region.name, "count": region.count}
        return Response(dic)


def create_first_check_item(user, check_project_id):
    current_check_project = CheckProject.objects.get(pk=check_project_id)
    check_time = add_time_interval(current_check_project.start_time)
    return CheckItem.objects.create(user=user, check_project=current_check_project, check_time=check_time,
                                    check_number=1)


def add_check_item(user, check_project_id):
    current_checkitems = CheckItem.objects.filter(check_project_id=check_project_id)
    if current_checkitems.count() == 0:
        return create_first_check_item(user, check_project_id)
    else:
        last_checkitem = current_checkitems.order_by('-check_time').first()
        return CheckItem.objects.create(user=user, check_project=check_project_id,
                                        check_time=add_time_interval(last_checkitem.check_time),
                                        check_number=last_checkitem.check_number + 1)

    # assert_equal(add_time_interval(time), datetime.datetime(2022, 3, 1, 8, 30))


class DiseaseListView(APIView):
    def get(self, request):
        diseases = Disease.objects.all()
        print(diseases)
        s = DiseaseSerializer(diseases, many=True)
        return Response(s.data)


class CheckItemListView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        # user info
        doctor = request.user
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 25))
        print(page)
        print(page_size)
        # username = "hi"
        # dept info
        site_name = "广州市妇幼保健院"
        check_name = ""

        # credit_info
        check_project = CheckProject.objects.get(pk=1)
        default_credit = check_project.credit
        left_credit = check_project.left_credit

        # count
        check_items = CheckItem.objects.filter(doctor=doctor)
        finish_items = check_items.exclude(status="Waiting")
        unfinish_items = check_items.filter(status="Waiting")
        all_item_count = check_items.count()
        finish_item_count = finish_items.count()
        unfinish_item_count = unfinish_items.count()

        # user's check item

        result = {
            "user": {
                "username": user.username
            },
            "department": {
                "site_name": site_name,
                "check_name": check_name
            },
            "credit": {
                "default_credit": default_credit,
                "left_credit": left_credit,
                "all_item_count": all_item_count,
                "finish_item_count": finish_item_count,
                "unfinish_item_count": unfinish_item_count
            },
            "item": [{
                "name": check_item.user.username,
                "phone": check_item.user.phone,
                "item_number": check_item.check_number,
                "start_time": check_item.check_date,
                "sex": check_item.user.sex,
                "age": check_item.user.age,
                "status": check_item.status,
                "id": check_item.id
            } for check_item in get_paginated_list(check_items, page, page_size)["items"]]
            ,
            "page-count": int(get_paginated_list(check_items, page, page_size)["total_pages"])
        }
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


class CheckUserDetail(APIView):
    def get(self, request):
        check_item_id = request.GET.get("check_item_id")
        check_item = CheckItem.objects.get(pk=check_item_id)
        user = check_item.user
        result = {
            "username": user.username,
            "age": user.age,
            "sex": user.sex,
            "check_number": check_item.check_number,
            "check_time": check_item.check_date
        }
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


class CheckReportDetail(APIView):
    permission_classes = ()

    def get(self, request):
        check_item_id = request.GET.get("check_item_id")
        check_item = CheckItem.objects.get(pk=check_item_id)
        report = check_item.check_report
        s = CheckReportSerializer(report)
        return Response(s.data)

    def post(self, request):
        s = CheckReportSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        check_item_id = request.GET.get("check_item_id")
        check_item = CheckItem.objects.get(pk=check_item_id)
        s = CheckReportSerializer(check_item, request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
