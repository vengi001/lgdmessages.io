from django.db import models

# Create your models here.
class MessageTable(models.Model):
    message = models.TextField()
    author = models.CharField(max_length=50)
    authoredDate = models.DateTimeField(auto_now_add=True)
    seenDate = models.DateTimeField(blank=True, null=True)
    readed = models.BooleanField(default=False)
    readBy = models.CharField(max_length=50, blank=True, null=True)
    authorizedTo = models.TextField()
    receivedDate = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'messages'

    def __str__(self):
        return self.author
        

class ReplyTable(models.Model):
    message = models.TextField()
    replyTo = models.ForeignKey(MessageTable, on_delete=models.CASCADE)
    repliedBy = models.CharField(max_length=50)
    repliedDate = models.DateTimeField(auto_now_add=True)
    main_message = models.TextField()

    class Meta:
        verbose_name_plural = 'replies'
    
    def __str__(self):
        return self.repliedBy

