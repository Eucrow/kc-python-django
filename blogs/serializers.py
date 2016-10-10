from rest_framework import serializers


class BlogSerializer(serializers.Serializer):

    username = serializers.CharField()

