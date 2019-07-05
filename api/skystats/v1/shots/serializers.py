from rest_framework import serializers

from .models import Shot


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        fields = "__all__"
