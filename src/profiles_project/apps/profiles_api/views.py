from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

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
