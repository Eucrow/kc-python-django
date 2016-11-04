from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):  # el PostSerializer.Meta dice que herede la clase Meta también del
                                # PostSerializer. Si no se pone, por defecto no la hereda
        fields = ("id", "title", "url", "introduction")
