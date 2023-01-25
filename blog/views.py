from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Count
from taggit.models import Tag
from pprint import pprint


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    trending_posts = Post.published.all().order_by('-publish')[:4]
    latest_post = Post.published.all().order_by('-publish')[:1]
    top_stories = Post.published.all().order_by('-publish')[5:9]
    similar_posts = Post.objects.prefetch_related().filter(tags__name__in=['Tech'])[:4]

    return render(request, 'blog/home.html', {'posts': posts, 'trending_posts': trending_posts, 'latest_post':latest_post, 'similar_posts': similar_posts})


