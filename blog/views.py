from django.shortcuts import render
from blog.models import Post, Author, Comment


def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        post.time_dif = post.published_recently()
    context = {
        'posts': posts
    }
    return render(
        request,
        'blog/post_list.html',
        context=context
    )


def post_by_author(request, author_id):
    posts = Post.objects.filter(author=author_id).all()
    
    for post in posts:
        post.time_dif = post.published_recently()
    context = {
        'posts': posts,
        'author': Author.objects.get(id=author_id)
    }
    return render(
        request,
        'blog/posts_by_author.html',
        context=context
    )


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(
        request,
        'blog/get_post.html',
        context=context
    )


