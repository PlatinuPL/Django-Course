from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data



# def index(request):
#     lastest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": lastest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts(request):
#     return render(request, "blog/posts.html",{
#         "all_posts": Post.objects.all().order_by("-date")
#     })


class SinglePostView(DetailView):
    template_name = "blog/single_post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
# def single_post(request,slug):
#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request, "blog/single_post.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })
