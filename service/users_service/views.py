

from .models import User, Camera
from rest_framework import generics

from .serializers import UserSerializer, CameraSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(email=self.request.user)


class CameraList(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CameraSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            # Return a empty query_set
            return []
        return Camera.objects.all().filter(user=self.request.user)
