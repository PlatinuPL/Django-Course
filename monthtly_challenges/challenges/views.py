from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'january': "Just eat healthy food!",
    'february': "Walk 20 minutes every each day!",
    'march': "Walk 20 minutes every each day!",
    'april': "Walk 20 minutes every each day!",
    'may':"Walk 20 minutes every each day!",
    'june': "Walk 20 minutes every each day!",
    'july': "Walk 20 minutes every each day!",
    'august': "Walk 20 minutes every each day!",
    'september': "Walk 20 minutes every each day!",
    'october': "Walk 20 minutes every each day!",
    'november': "Walk 20 minutes every each day!",
    'december': "Walk 20 minutes every each day!"
}

def index(request):
    response_data = '''
        <ul>
            <li><a href="/challenges/january">January</a></li>
        </ul>'''
    return HttpResponse()

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args= [redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
