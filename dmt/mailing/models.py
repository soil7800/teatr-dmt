from django.db import models


class Subscriber(models.Model):

    name = models.CharField("Имя", max_length=200)
    email = models.EmailField("Email")
    sendpulse_status = models.BooleanField('Подключен к sendpulse', default=False, editable=None)
    
    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"