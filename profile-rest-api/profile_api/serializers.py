from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name filed for tetsing our APIView"""
    name = serializers.CharField(max_length=10)
    
#model serializare

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
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


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile' , 'status_text' , 'created_on')
        #user_profile is read-only
        extra_kwargs = {'user_profile': {'read_only': True}} #extra key arguments 

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'