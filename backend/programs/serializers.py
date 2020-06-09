from rest_framework import serializers

from .models import Program


class ProgramSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    is_active = serializers.BooleanField()
    name = serializers.CharField()

    class Meta:
        model = Program
        fields = [
            'id',
            'is_active',
            'name',
        ]

    extra_kwargs = {
        "id": {"required": False},
        "is_active": {"required": False},
        "name": {"required": True},
    }


