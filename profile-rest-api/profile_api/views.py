from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profile_api import serializers


class HelloApiView(APIView):
    """Test API VIew"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you applocation logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create an hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(): #daca inputul este valid
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST) #for user when tries to submmit an invalid input
# Create your views here.
