from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Test Serializer"""

    name = serializers.CharField(max_length=10)
    