from django.urls import path, include
from chat import views

urlpatterns = [
     path('reg/', views.CreateUser.as_view()),
     path('create_chat/', views.ChatList.as_view()),
     path('messages/', views.MessageList.as_view()),
]
