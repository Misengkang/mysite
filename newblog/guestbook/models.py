from django.db import models


class Message(models.Model):
    visitor_name = models.CharField(max_length=25)
    visitor_email = models.EmailField(max_length=255)
    visitor_url = models.URLField(blank=True)
    message_text = models.TextField(max_length=256)
    message_time = models.DateTimeField(auto_now_add=True)

    # 为了显示
    def __str__(self):
        return self.message_text[:20]
