from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)# имя статьи
    body = models.TextField() # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
