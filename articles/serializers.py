from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.author.email
        
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.author.email

    class Meta:
        model = Article
        fields = ("pk", "title", "author")


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content")
