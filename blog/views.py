from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Count
import random
from taggit.models import Tag
from pprint import pprint


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    top_stories = random.sample(list(posts), 4)
    trending_posts = Post.published.all().order_by('-publish')[:4]
    latest_post = Post.published.all().order_by('-publish')[:1]
    politics_posts = Post.published.prefetch_related().filter(tags__name__in=['Politics'])[:4]
    entertainment_posts = Post.published.prefetch_related().filter(tags__name__in=['Entertainment'])[:4]
    tech_posts = Post.published.prefetch_related().filter(tags__name__in=['Tech'])[:4]

    return render(request, 
                'blog/home.html', 
                {'posts': posts, 
                'trending_posts': trending_posts, 
                'latest_post':latest_post, 
                'politics_posts': politics_posts,
                'top_stories': top_stories,
                'politics_posts': politics_posts,
                'entertainment_posts': entertainment_posts,
                'tech_posts': tech_posts})

