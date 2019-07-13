from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Session, Shot

import logging

logger = logging.getLogger(__name__)


class ShotSerializer(serializers.ModelSerializer):
    session = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shot
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True)

    class Meta:
        model = Session
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Session.objects.all(), fields=("timestamp", "session_type")
            )
        ]

    def create(self, validated_data):
        shots = validated_data.pop("shots")
        session = Session.objects.create(**validated_data)
        for shot in shots:
            Shot.objects.create(session=session, **shot)
        return session
