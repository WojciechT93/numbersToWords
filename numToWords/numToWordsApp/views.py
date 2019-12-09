from django.shortcuts import render

from django.http import HttpResponse
from .forms import chooseNumberForm 
from django.template import loader
from num2words import num2words

def chooseNumber(request):
    form = chooseNumberForm()
    context = {"form" : form}
    template = loader.get_template('chooseNumber.html')
    return HttpResponse(template.render(context))

def result(request):
    if request.method == "GET":
        form = chooseNumberForm(request.GET)
        numberWord = num2words(form.number)
        context = {"numberWord" : numberWord}
        if form.is_valid():
            template = loader.get_template('result.html')
            return HttpResponse(template.render(context))

    form = chooseNumberForm()
    context = {"form" : form}
    template = loader.get_template('chooseNumber.html')
    return HttpResponse(template.render(context))