from rest_framework import serializers

from .models import Program


class ProgramSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)
    name = serializers.CharField(required=True)

    class Meta:
        model = Program
        fields = [
            'id',
            'is_active',
            'name',
        ]



