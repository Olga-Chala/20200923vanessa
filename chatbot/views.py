from django.shortcuts import render
from django.http import HttpResponse
from .models import VanessaModule
from chatbot.logic_implement.vanessa_talking import say

# def abc_modules_list(request):
#     a=0
#     # return HttpResponse(VanessaModule.objects.filter(module_number__exact=a).values())
#     return HttpResponse(VanessaModule.objects.get(module_number__exact=a).vanessa_question)
    # return HttpResponse("...to be continued")


def talk (request):
    a = 4 
    say(VanessaModule.objects.get(module_number__exact=a).vanessa_question)
    return HttpResponse("...to be continued")
