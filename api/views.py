from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# obtain_auth_token = ObtainAuthToken.as_view()
from api.models import User


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
