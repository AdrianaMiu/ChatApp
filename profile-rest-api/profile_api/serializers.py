from rest_framework import serializers
from profile_api import models
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
         )
        return user
    #override updated password to add  this logic for the pass in validated_data
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

"""
class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile' , 'status_text' , 'created_on')
        #user_profile is read-only
        extra_kwargs = {'user_profile': {'read_only': True}} #extra key arguments 
"""
class MessageSerializer(serializers.Serializer): #ModelSerializer asks for class Meta
    """Serializes a message"""
    username = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=2048)
