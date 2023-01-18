from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="ads")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comment_author")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
