from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        