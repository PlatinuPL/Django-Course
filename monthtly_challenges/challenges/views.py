from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    'january': "Just eat healthy food!",
    'february': "Walk 20 minutes every each day!",
    'march': "Walk 20 minutes every each day!",
    'april': "Walk 20 minutes every each day!",
    'may':"Walk 20 minutes every each day!",
    'june': "Walk 20 minutes every each day!",
    'july': None,
    'august': "Walk 20 minutes every each day!",
    'september': "Walk 20 minutes every each day!",
    'october': "Walk 20 minutes every each day!",
    'november': "Walk 20 minutes every each day!",
    'december': "Walk 20 minutes every each day!"

}

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months # przekazanie znimennej months do pliku html

    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args= [redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try: 
       # month_text = month.capitalize()
        challenge_text = monthly_challenges[month]
        response_data = render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month": month
        })
        return HttpResponse(response_data)
    except:
        raise Http404()
    
