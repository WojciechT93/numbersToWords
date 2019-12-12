from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import random
import sys

from .forms import ChooseNumberForm 
from num2words import num2words
from .numbersToWords import *
from . import views

# Create your tests here.

class GetWordsRepresentationTestCase(TestCase):

    def test_get_words_representation_function(self):
        test_numbers_results = [[0, 'zero'], [5, 'pięć'], [10, 'dziesięć'], [13, 'trzynaście'], [58, 'pięćdziesiąt osiem'], 
                            [240, 'dwieście czterdzieści'], [999, 'dziewięćset dziewięćdziesiąt dziewięć'], 
                            [1000, 'tysiąc'], [1898, 'tysiąc osiemset dziewięćdziesiąt osiem'], 
                            [3243451,'trzy miliony dwieście czterdzieści trzy tysiące czterysta pięćdziesiąt jeden']]
        for test_set in test_numbers_results:
            result = get_words_representation(test_set[0])
            self.assertEqual(result, test_set[1])
    
    # This might be not best way to test my getWordsRepresentation() because it is also testing results of num2words
    # Found mistake in numbers2words lib. 90 is 'dziewięćdzisiąt' instead of 'dziewięćdziesiąt'
    def test_compare_library_num2words_with_get_words_representation_results(self):
        for i in range(100000):
            random_number = random.randint(0, 999999999999999999)
            result_1 = get_words_representation(random_number)
            result_2 = num2words(random_number, lang='pl')
            self.assertEqual(result_1, result_2)

    def test_pass_wrong_type_value_to_get_words_representation(self):
        test_values = ['abc', -32, '-1', 0.5, True]
        for test_value in test_values:
            result = get_words_representation(test_value)
            self.assertEqual(result, '') 

class ChooseNumberTestCase(TestCase):
    def test_result_correct_request_response(self):
        response = self.client.get('/numToWordsApp/result/?number=4124')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['numberWord'], 'cztery tysiące sto dwadzieścia cztery')

    def test_result_wrong_request_response(self):
        response = self.client.get('/numToWordsApp/result/?number=dasd')
        self.assertEqual(response.status_code, 406)
        response2 = self.client.get('/numToWordsApp/result/?number=-123')
        self.assertEqual(response2.status_code, 406)
        response3 = self.client.post('/numToWordsApp/result/', {'number' : '1231'})
        self.assertEqual(response3.status_code, 406)