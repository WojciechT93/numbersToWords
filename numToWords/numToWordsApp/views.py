from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import ChooseNumberForm 
from num2words import num2words
from .numbersToWords import *

TEMPLATES = {
    'chooseNumber' : 'chooseNumber.html',
    'result' : 'result.html'
}

def choose_number(request):
    form = ChooseNumberForm()
    context = {"form" : form}
    template = loader.get_template(TEMPLATES['chooseNumber'])
    return HttpResponse(template.render(context))

def result(request):
    if request.method == "GET":
        form = ChooseNumberForm(request.GET)
        if form.is_valid():
            if form['number'].data:
                number = form['number'].data
                if str(number).isdigit():
                    number = int(number)
                else:
                    return HttpResponse(status = 406)
                # W komentarzu poniżej wersja z użyciem gotowej biblioteki num2words.
                # numberWord = num2words(number, lang = 'pl') 
                number_word = get_words_representation(number)
                context = {"numberWord" : number_word}
                template = loader.get_template(TEMPLATES['result'])
                return HttpResponse(template.render(context))
    return HttpResponse(status = 406)