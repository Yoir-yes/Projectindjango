from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .models import Post


class post_list(ListView):
    model = Post
    paginate_by = 8
    template_name = 'project/post/list.html'

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
    fields = ['tytul','tresc','status']

    def form_valid(self, form):
        note = form.save()
        return redirect('project:detail', pk=note.pk)