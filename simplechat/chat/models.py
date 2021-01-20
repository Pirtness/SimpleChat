from django.db import models

#юзер с именем логином и паролем (стандартный)

#чат (юзер1 юзер2)
class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey('auth.User', related_name='chats1', on_delete=models.CASCADE)
    user2 = models.ForeignKey('auth.User', related_name='chats2', on_delete=models.CASCADE)

    #def save(self, *args, **kwargs):

    class Meta:
        ordering = ['created']


#сообщения (текст, дата, создатель, кому)
class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message_text = models.CharField(max_length=300, blank=False)
    author = models.ForeignKey('auth.User', related_name='messages_author', on_delete=models.CASCADE)
    chat_id = models.ForeignKey('Chat', related_name='messages_dialog', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
