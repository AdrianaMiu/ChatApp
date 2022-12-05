from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication #creeaza un token random de fiecare dsts cand userul se logheaza si acest token este adaugat la fiecare request efectuat de user
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


#profile_api
from profile_api import serializers, models, permissions

#elastic
from elasticsearch_app import *

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer #object
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication , ) # virgula pt o tupla in loc de un sg item
#specifica cum user se va autentifica
    permission_classes = (permissions.UpdateOwnProfile ,) 
    #ce poate userul sa faca
    filter_backends = ( filters.SearchFilter,)
    search_fields = ('username', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

"""
class UserProfileFeedViewSet(viewsets.ModelViewSet):
   
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnSTatus, 
        IsAuthenticatedOrReadOnly,
    )


    def perform_create(self, serializer):
        
        serializer.save(user_profile=self.request.user)
"""

class MessageApiView(GenericAPIView):
    """Messages endpoint"""

    serializer_class = serializers.MessageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ""

    def get(self, request, format=None):
        username = request.user.username
        return Response(get_messages(es=es, username=username))
        
        
    def post(self, request):
        serializer=self.serializer_class(data=request.data) 
        if serializer.is_valid():
            username_src = request.user.username #userul logat 
            username_dest = serializer.validated_data.get('username')
            message = serializer.validated_data.get('message')
            if models.UserProfile.objects.filter(username=username_dest).exists() and username_src != username_dest:
                send_messages(es=es, username_src=username_src, username_dest=username_dest, message=message)
                return Response({'username_src': username_src, 'username_dest': username_dest, 'message': message})
            elif username_src == username_dest:
                return Response('You cannot send message to yourself!', status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response(f'User {username_dest} does not exist!', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 