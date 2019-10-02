from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
from Insta.models import Post
from django.urls import reverse_lazy
class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__'
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ('title',)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')