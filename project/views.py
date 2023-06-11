from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .models import Post
from .filters import PostFilter
from django.core.paginator import Paginator

class post_list(ListView):
    model = Post
    filter_class = PostFilter
    paginate_by = 8
    template_name = 'project/post/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context
class post_detail(DetailView):
    model = Post
    template_name = 'project/post/detail.html'
class add_post(CreateView):
    model = Post
    template_name = 'project/post/addpost.html'
    fields = '__all__'

    def form_valid(self, form):
        note = form.save()
        return redirect('project:detail', pk=note.pk)

class update_post(UpdateView):
    model = Post
    template_name = 'project/post/updatingpost.html'
    fields = ['tytul','tresc','priorytet']

    def form_valid(self, form):
        note = form.save()
        return redirect('project:detail', pk=note.pk)