from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
    )
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(default=timezone.now())
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.tytul