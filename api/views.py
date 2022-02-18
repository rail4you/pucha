from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# obtain_auth_token = ObtainAuthToken.as_view()
from api.models import CheckItem, CheckProject, Region, User
from api.utils import add_time_interval


class ObtainAuthToken(APIView):
    permission_classes = ()  # <-- And here

    def post(self, request, *args, **kwargs):
        dic = request.data
        user, _ = User.objects.get_or_create(username=dic["username"], phone=dic["phone"], card_id=dic["card_id"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


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
