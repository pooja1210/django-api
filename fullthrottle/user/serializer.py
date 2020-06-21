from rest_framework import routers, serializers, viewsets
from . models import User, ActivityPeriod

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['user_id', 'start_time', 'end_time']
        read_only_fields = ('user_id',)

class UserSerializer(serializers.ModelSerializer):
    activity_period = ActivitySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['user_id', 'real_name', 'address', 'activity_period']

