from rest_framework import serializers

from api.models import User, Disease, CheckReport


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = "__all__"


class CheckReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckReport
        fields = "__all__"
