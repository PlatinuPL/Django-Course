from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Post,Author,Tag


# Create your views here.
def index(request):
    lastest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": lastest_posts
    })


def posts(request):
    return render(request, "blog/posts.html",{
        "all_posts": Post.objects.all().order_by("-date")
    })

def single_post(request,slug):
    identified_post = get_object_or_404(Post,slug=slug)
    return render(request, "blog/single_post.html", {
        "post": identified_post
    })
