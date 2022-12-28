from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review
# Create your views here.



class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thankk-you"


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thankk-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form})
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")

def review (request):
    if request.method == "POST":
        #existing_model = Review.objects.get(pk=1) - jeżeli chcesz dodac nowy element w miejsce istniejącego
        form = ReviewForm(request.POST) # , instance= existing_model - jeżeli chcesz dodac nowy element w miejsce istniejącego
        
        if form.is_valid():
            #review = Review(
                # user_name = form.cleaned_data['user_name'],
                # review_text = form.cleaned_data["review_text"],
                # rating = form.cleaned_data['rating'])
            #review.save()
            form.save()
            return HttpResponseRedirect("thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thanks.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['massage'] = "This works!"
        return context 


class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data



# class ReviewListView(TemplateView):
#     template_name = "reviews/reviews_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
 
# def thankyou(request):
#     return render(request, "reviews/thanks.html")

class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/review/reviews/" + review_id)