from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm

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


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/single_post.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # możemy zapisć bo typ Form to MODELFORM
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("singpo", args=[slug]))
        
        post = Post.objects.get(slug=slug)
        context = {
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": comment_form,
                "comments": post.comments.all().order_by("-id")
            }
        return render(request, "blog/single_post.html", context)

class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts") 

        context= {}

        if stored_posts is None or len(stored_posts) == 0:      
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored_posts.html",context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context

# def single_post(request,slug):
#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request, "blog/single_post.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })
