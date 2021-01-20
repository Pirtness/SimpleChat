from rest_framework import serializers
from chat.models import Chat, Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ChatSerializer(serializers.ModelSerializer):
    user1 = serializers.ReadOnlyField(source='user1.username')
    user2 = serializers.ReadOnlyField(source='user2.username')
    messages_dialog = serializers.StringRelatedField(many=True, default=[])

    class Meta:
        model = Chat
        #fields=['id', 'user1', 'user2']
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    chat_id = serializers.ReadOnlyField(source='chat_id.id')

    class Meta:
        model = Message
        fields = ['message_text', 'author', 'chat_id']


UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    messages_author = serializers.StringRelatedField(many=True, default=[])
    chats1 = serializers.StringRelatedField(many=True, default=[])
    chats2 = serializers.StringRelatedField(many=True, default=[])

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        #fields = ['id', 'username']
        fields = '__all__'
