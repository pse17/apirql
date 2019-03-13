from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    Serialize user instance to JSON format
    '''
    class Meta:
        model = User
        fields  = ('id', 'username', 'email')

