from django.shortcuts import render
from .models import User, ActivityPeriod
from rest_framework import viewsets
from.serializer import UserSerializer, ActivitySerializer
from rest_framework.decorators import action

# Create your views here.


def user_list(request):
    user = User.objects.all()
    activity_list = []
    for i in user:
        activity = ActivityPeriod.objects.filter(user_id = i.id)
        print("@@@", activity)
        # activity_list = activity_list.append(activity)   
    context = {
        "user": user,
        "activity": activity
    }
    
    return render(request,'list.html',context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail =True, methods = ["GET"])
    def activiyt(self):
        user_id = self.get_object()
        qs = ActivityPeriod.objects.filter(user_id=user_id)
        serializer =  ActivitySerializer(qs,many=True)
        return response(serializer.data, status=200)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivitySerializer
