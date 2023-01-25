from django.shortcuts import render
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
    # post_tags_id = posts.tags.value_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__post=posts).annotate()
    # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    tech_post = Post.published.filter(tag_slug=['politics'])
    
    return render(request, 'blog/home.html', {'posts': posts, 'trending_posts': trending_posts, 'latest_post':latest_post, 'tech_post': tech_post })


