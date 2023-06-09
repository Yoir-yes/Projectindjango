import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):


    priorytet = django_filters.ChoiceFilter(choices = Post.STATUS_CHOICES)
    class Meta:
        model = Post
        fields = ['priorytet']