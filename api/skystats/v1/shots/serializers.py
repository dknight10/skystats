from typing import Any, Dict

from rest_framework import serializers

from .models import Session, Shot

import logging

logger = logging.getLogger(__name__)


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        exclude = ("session",)


class SessionSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True)

    class Meta:
        model = Session
        fields = "__all__"

    def create(self, validated_data):
        shots = validated_data.pop("shots")
        session = Session.objects.create(**validated_data)
        for shot in shots:
            Shot.objects.create(session=session, **shot)
        return session
