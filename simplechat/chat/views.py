
from rest_framework import generics
from chat.models import Chat, Message
from chat.serializers import ChatSerializer, MessageSerializer, UserSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import permissions



class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Chat.objects.filter(user1=self.request.user,
        user2=get_user_model().objects.get(username = self.request.data['reciever'])) | Chat.objects.filter(user2=self.request.user,
        user1=get_user_model().objects.get(username = self.request.data['reciever']))
        return queryset

    def perform_create(self, serializer):
        qyeryset = Chat.objects.filter(user1=self.request.user,
        user2=get_user_model().objects.get(username = self.request.data['reciever'])) | Chat.objects.filter(user2=self.request.user,
        user1=get_user_model().objects.get(username = self.request.data['reciever']))

        if len(qyeryset) == 0:
            serializer.save(user1=self.request.user,
                user2=get_user_model().objects.get(username = self.request.data['reciever']))

class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Chat.objects.filter(user1=self.request.user,
        user2=get_user_model().objects.get(username = self.request.data['reciever'])) | Chat.objects.filter(user2=self.request.user,
        user1=get_user_model().objects.get(username = self.request.data['reciever']))

        queryset = Message.objects.filter(chat_id=queryset[0])#.values('message_text', 'author')
        return queryset

        #if len(queryset) == 0:
        #    print("не создан")

    def perform_create(self, serializer):
        queryset = Chat.objects.filter(user1=self.request.user,
        user2=get_user_model().objects.get(username = self.request.data['reciever'])) | Chat.objects.filter(user2=self.request.user,
        user1=get_user_model().objects.get(username = self.request.data['reciever']))

        if len(queryset) == 0:
            ChatSerializer.save(user1=self.request.user,
                user2=get_user_model().objects.get(username = self.request.data['reciever']))

        queryset = Chat.objects.filter(user1=self.request.user,
        user2=get_user_model().objects.get(username = self.request.data['reciever']))| Chat.objects.filter(user2=self.request.user,
        user1=get_user_model().objects.get(username = self.request.data['reciever']))
        #queryset = Message.objects.filter(chat_id=queryset[0])
        serializer.save(message_text = self.request.data.get('message_text'),
        author = self.request.user, chat_id = queryset[0])



class CreateUser(generics.CreateAPIView):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
