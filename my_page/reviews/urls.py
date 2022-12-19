from django.urls import path


from . import views

urlpatterns = [
    path("", views.review),
    path("class", views.ReviewView.as_view()),
    path("thank-you", views.thankyou)

]
