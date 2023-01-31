from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Count
import random
from taggit.models import Tag



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





def post_detail(request, year, month, day, post):
    post =  get_object_or_404(Post, 
                                slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    post_tags_id = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:6]
    return render(request, 'blog/detail.html', {'post': post, 'similar_posts': similar_posts})


