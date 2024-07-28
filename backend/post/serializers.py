from rest_framework import serializers
from .models import Posts, Comment


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    total_comment = serializers.SerializerMethodField('total_comment_per_post')
    comments = CommentsSerializer(many=True, read_only=True)

    def total_comment_per_post(self, instance):
        total_comment = instance.comments.all().count()
        return total_comment

    def comments_list(self, instance):
        all_comments_list = instance.comments.all()
        return all_comments_list

    class Meta:
        model = Posts
        fields = '__all__'



