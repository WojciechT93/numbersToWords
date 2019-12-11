from django.shortcuts import render

from django.http import HttpResponse
from .forms import chooseNumberForm 
from django.template import loader
from num2words import num2words
from .numbersToWords import *

def chooseNumber(request):
    form = chooseNumberForm()
    context = {"form" : form}
    template = loader.get_template('chooseNumber.html')
    return HttpResponse(template.render(context))

def result(request):
    if request.method == "GET":
        form = chooseNumberForm(request.GET)
        number = form['number'].data
        # W komentarzu poniżej wersja z użyciem gotowej biblioteki num2words.
        # numberWord = num2words(number, lang = 'pl') 
        numberWord = getWordsRepresentation(number)
        context = {"numberWord" : numberWord}
        if form.is_valid():
            template = loader.get_template('result.html')
            return HttpResponse(template.render(context))

    form = chooseNumberForm()
    context = {"form" : form}
    template = loader.get_template('chooseNumber.html')
    return HttpResponse(template.render(context))