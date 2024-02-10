from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name='post_list'),
    path("author/<int:author_id>", blog_views.post_by_author, name='post_by_author'),
    path("get_post/<int:post_id>", blog_views.get_post, name='get_post')
]

