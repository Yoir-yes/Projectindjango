from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class Post(models.Model):
    STATUS_CHOICES = (
        ('very important', 'Bardzo Ważne'),
        ('important','Ważne'),
        ('not as important', 'Nie tak ważne'),
        ('not important', 'Nieważne'),
    )
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(default=timezone.now())
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    priorytet = models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.tytul
    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))


