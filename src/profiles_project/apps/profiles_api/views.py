from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.

# def hello_world(self, request, )

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_api_view = [
            'who cares',
            'for reals',
            'who really cares',
            'gives most control over your logic'
        ]
        return Response({'message': "Success", 'data': an_api_view})

    def post(self, request):
        """Create a greeting with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            msg = "Hello {}!".format(name)
            return Response({'message': msg})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles patching"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes"""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """List some things"""

        an_api_viewset = [
            'who cares',
            'for reals',
            'who really cares',
            'gives most control over your logic'
        ]
        return Response({'message': "Success", 'data': an_api_viewset})

    def create(self, request):
        """Testing create func from viewset"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {}".format(name)
            return Response({'message': msg})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting a single object"""

        return Response({'method': 'get'})

    def update(self, request, pk=None):
        """Updates an object"""

        return Response({'method': 'put'})

    def partial_update(self, request, pk=None):
        """partial update"""

        return Response({'method', 'patch'})

    def destroy(self, request, pk=None):
        """Delete"""

        return Response({'method', 'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles CRUD for the user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', )

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use the obtain auth token api view to validate and create a token"""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save(user_profile = self.request.user)