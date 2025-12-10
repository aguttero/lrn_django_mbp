from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page_url"),
    path("posts", views.posts, name="posts_url"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail_url")
]