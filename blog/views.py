from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    trending_posts = Post.published.all().order_by('-publish')[:4]
    latest_post = Post.published.all().order_by('-publish')[:1]
    top_stories = Post.published.all().order_by('-publish')[5:9]
    return render(request, 'blog/home.html', {'posts': posts, 'trending_posts': trending_posts, 'latest_post':latest_post, 'top_stories': top_stories})
