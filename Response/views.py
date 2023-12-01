from faker import Faker
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from sources.patterns import fake_possible_values
from sources.fake_funtions import make_fake_value_as_label, Provider
from .response import get_answer
from sources.checks import GetRes
from sources.text_funtions import text_operations, correct_text, find_corrected_words

class SendResponse(APIView):    
    def post(self,request):
        input_ = request.data['query']
        data = GetRes(input_)
        return Response(data)

class ColorsView(APIView):
    def get(self,request):
        data = open('Response/files/colors.json')
        data = json.load(data)
        colors_data = []
        for i in range(len(data['Name'])):
            obj = {
                'label':data['Name'][str(i)],
                'value':data['hex'][str(i)],
                'rgb':data['rgb'][str(i)]
            }            
            colors_data.append(obj)
        return Response(colors_data)
    
class TextOperations(APIView):
    def post(self, request):
        text = request.data['text']
        aggr = text_operations(text)
        crt,corrections = find_corrected_words(text)
        return Response({'aggregation': aggr, 'corrected':crt,'corrections':corrections, 'tokenization': ''})
        
        
class FakeValues(APIView):
    def get(self, request):
        filterd_fake_possible_values = []
        for value in fake_possible_values:
            obj = {
                'label': make_fake_value_as_label(value),
                'value' : value
            }
            filterd_fake_possible_values.append(obj)
        return Response(filterd_fake_possible_values)        
    def post(self, request):
        value = request.data.get('value')
        fake = Faker()
        fake.add_provider(Provider)
        value = getattr(fake, value)()
        return Response(value)        
