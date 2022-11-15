from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name filed for tetsing our APIView"""
    name = serializers.CharField(max_length=10)
    
