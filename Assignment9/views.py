from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# This view shows all users and allows creating new user
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# This view handles get, update and delete for single user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer