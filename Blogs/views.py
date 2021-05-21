from Blogs.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm
from .models import Comment, Post
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
 #   return render(request, 'home.html',{})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'
   #fields = '__all__'
   #fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    #fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm 
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
      
    success_url = reverse_lazy('home')
    #fields = '__all__'