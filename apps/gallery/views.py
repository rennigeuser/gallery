from django.shortcuts import render
from .models import Post
from django.http import JsonResponse


def main_page(request):
    return render(request, 'gallery/main.jinja')


def get_posts(request):
    posts = [
        {
        'title': post.title,
        'author_email': post.author.email,
        'icon_link': post.icon.image.url,
        'alt': post.icon_alt,
        'likes': post.likes,
        'created_at': post.created_at,
        } for post in Post.objects.all()]

    return JsonResponse({'posts': posts})